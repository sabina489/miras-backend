from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Role, Profile

User = get_user_model()


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('faculty','college_name','admission_year')


class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = User
        fields = ('phone', 'first_name', 'last_name',
                  'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.role.add(Role.objects.get(id=1))
        for attr, value in profile.items():
            setattr(user.profile, attr, value)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileCreateSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        instance = super().update(instance, validated_data)
        for attr, value in profile.items():
            setattr(instance.profile, attr, value)
        instance.profile.save()
        return instance


class UserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone')
        extra_kwargs = {'id': {'read_only': True}}
