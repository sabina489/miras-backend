from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.models import Role, Profile
from django.forms import ValidationError
from django.conf import settings
from django.db import transaction
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from common.utils import send_mail_common, send_otp
from random import randrange

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('faculty', 'college_name', 'admission_year',
                  'extra_content', 'image',)


class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer(required=False)

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name',
                  'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        profile = None
        if 'profile' in validated_data:
            profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.role.add(Role.objects.get(id=1))
        user.is_active = False
        if profile:
            interests = None
            if 'interests' in profile:
                interests = profile.pop('interests')
            profile_object = Profile.objects.create(user=user)
            for attr, value in profile.items():
                setattr(profile_object, attr, value)
            if interests:
                profile_object.interests.set(interests)
            profile_object.save()
        user.otp = randrange(100000, 999999)
        user.otp_expiry = timezone.now()+timezone.timedelta(seconds=settings.OTP_EXPIRY_SECONDS)

        user.save()

        send_mail_common('accounts/email/activate.html', {
            'user': user,
            'domain': settings.FRONTEND_URL,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'otp': user.otp,
        }, [user.email], 'Activate your account')
        send_otp(user.phone, user.otp, user.otp_expiry)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')

    def update(self, instance, validated_data):
        profile = None
        if 'profile' in validated_data:
            profile = validated_data.pop('profile')
        instance = super().update(instance, validated_data)
        if profile:
            if 'interests' in profile:
                interests = profile.pop('interests')
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
    class Meta:
        model = User
        fields = ('id', 'otp')
        extra_kwargs = {'otp': {'write_only': True}}

    def validate_otp(self, value):
        otp_time_valid = self.instance.is_otp_time_valid
        valid_otp = self.instance.validate_otp(value)
        if otp_time_valid and valid_otp:
            return value
        else:
            raise ValidationError("OTP expired or invalid")
