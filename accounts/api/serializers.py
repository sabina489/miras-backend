from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Role, Profile
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('faculty','college_name','admission_year')


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
        user.is_active = False
        if profile:
            for attr, value in profile.items():
                setattr(user.profile, attr, value)
        user.save()
        # send email to activate user
        mail_subject = 'Activate your account.'
        message = render_to_string('accounts/email/activate.html', {
            'user': user,
            'domain': 'http://localhost:3000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = user.email
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
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
        fields = ('id', 'first_name', 'last_name', 'phone')
        extra_kwargs = {'id': {'read_only': True}}


class UserActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_active')