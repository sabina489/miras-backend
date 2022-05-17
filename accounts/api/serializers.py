from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.models import Role, Profile
from common.models import OTP
from django.forms import ValidationError
from django.conf import settings
from django.db import transaction
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from common.utils import send_mail_common, send_otp
from random import randrange
from accounts.api.utils import get_tokens_for_user
User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('faculty', 'college_name', 'admission_year',
                  'extra_content', 'image',)


class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer(required=False)
    token = serializers.SerializerMethodField(read_only=True)
    otp = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name',
                  'email', 'password', 'profile', 'otp', "token")
        extra_kwargs = {'password': {'write_only': True}}

    def validate_otp(self, value):
        try:
            otp = OTP.objects.filter(
                phone=self.initial_data['phone']).last()
        except:
            raise ValidationError('OTP not found')
        if otp.otp == int(value) and otp.otp_expiry > timezone.now():
            return value
        else:
            raise ValidationError("OTP expired or invalid")

    @transaction.atomic
    def create(self, validated_data):
        profile = None
        if 'profile' in validated_data:
            profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.role.add(Role.objects.get(id=1))
        user.is_active = True
        if profile:
            interests = profile.pop(
                'interests') if 'interests' in profile else None
            profile_object = Profile.objects.create(user=user)
            for attr, value in profile.items():
                setattr(profile_object, attr, value)
            if interests:
                profile_object.interests.set(interests)
            profile_object.save()
        # user.otp = randrange(100000, 999999)
        # user.otp_expiry = timezone.now()+timezone.timedelta(seconds=settings.OTP_EXPIRY_SECONDS)

        user.save()

        # send_otp(user.phone, user.otp, user.otp_expiry)
        return user

    def get_token(self, obj):
        return get_tokens_for_user(obj)


class UserSendOTPSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer(required=False)

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name',
                  'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def send_otp(self):
        otp = randrange(100000, 999999)
        otp_expiry = timezone.now()+timezone.timedelta(seconds=settings.OTP_EXPIRY_SECONDS)
        send_otp(self.validated_data['phone'], otp, otp_expiry)
        return True


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile')

    def update(self, instance, validated_data):
        profile = None
        if 'profile' in validated_data:
            profile = validated_data.pop('profile')
        instance = super().update(instance, validated_data)
        if profile:
            interests = profile.pop(
                'interests') if 'interests' in profile else None
            for attr, value in profile.items():
                setattr(instance.profile, attr, value)
            if interests:
                instance.profile.interests.set(interests)
            instance.profile.save()
        return instance


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email')
        extra_kwargs = {'id': {'read_only': True}}


class UserActivateSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField(required=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'otp', 'token')

    def validate_otp(self, value):
        otp_time_valid = self.instance.is_otp_time_valid
        valid_otp = self.instance.validate_otp(value)
        if otp_time_valid and valid_otp:
            return value
        else:
            raise ValidationError("OTP expired or invalid")

    def update(self, instance, validated_data):
        instance.is_active = True
        instance.otp_expiry = timezone.now()
        instance.save()
        return instance

    def get_token(self, obj):
        return get_tokens_for_user(obj)


class UserResetPasswordRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'phone')

    def validate_phone(self, value):
        if self.instance.phone == value:
            return value
        else:
            raise ValidationError("Phone does not match")

    def update(self, instance, validated_data):
        instance.otp_reset = randrange(100000, 999999)
        instance.otp_reset_expiry = timezone.now(
        )+timezone.timedelta(seconds=settings.OTP_EXPIRY_SECONDS)
        instance.reset_token = default_token_generator.make_token(instance)
        instance.save()
        send_mail_common('accounts/email/reset_password.html', {
            'user': instance,
            'domain': settings.FRONTEND_URL,
            'token': instance.reset_token,
            'otp': instance.otp_reset,
        }, [instance.email], 'Reset your password')
        send_otp(instance.phone, instance.otp_reset, instance.otp_reset_expiry)
        return instance


class UserResetPasswordConfirmSerializer(serializers.ModelSerializer):
    reset_token = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'reset_token', 'password', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_reset_token(self, value):
        if default_token_generator.check_token(self.instance, value):
            return value
        else:
            raise ValidationError("Invalid reset token")

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserResetPasswordOTPConfirmSerializer(serializers.ModelSerializer):
    otp_reset = serializers.IntegerField(required=True)
    reset_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'otp_reset', 'reset_token', 'phone')

    def validate_otp_reset(self, value):
        otp_time_valid = self.instance.is_otp_reset_time_valid
        valid_otp = self.instance.validate_otp_reset(value)
        if otp_time_valid and valid_otp:
            return value
        else:
            raise ValidationError("OTP expired or invalid")

    def update(self, instance, validated_data):
        pass
