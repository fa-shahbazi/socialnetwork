from accounts.models import Profile
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'age',
            'bio',
            'phone_number',
            'location',
            'gender',
            'avatar',

        )
        extra_kwargs = {
            'user': {'required': False},
            'avatar': {'required': False},
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile']

    extra_kwargs = {
        'password': {'write_only': True},
        'is_staff': {'read_only': True},
        'is_admin': {'read_only': True},
    }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context['request']
        Token.objects.get_or_create(user=instance)
        if request.user == instance:
            data['token'] = instance.auth_token.key
        return data


