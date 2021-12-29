from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

from accounts.models import Role, Profile
from django.conf import settings
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
                  'interests', 'extra_content')


class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer(required=False)

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name',
                  'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = None
        if 'profile' in validated_data:
            profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.role.add(Role.objects.get(id=1))
        user.is_active = True
        if profile:
            for attr, value in profile.items():
                setattr(user.profile, attr, value)
        user.otp = randrange(100000, 999999)
        user.otp_expiry = timezone.datetime.now()+timezone.timedelta(days=settings.OTP_EXPIRY_DAYS)
        user.save()
        send_mail_common('accounts/email/activate.html', {
            'user': user,
            'domain': 'localhost:3000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        }, [user.email], 'Activate your account')
        send_otp(user.phone, user.otp)
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
            for attr, value in profile.items():
                setattr(instance.profile, attr, value)
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
        fields = ('id', 'is_active')
