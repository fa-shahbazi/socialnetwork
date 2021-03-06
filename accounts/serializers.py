from accounts.models import Profile
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

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




class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile']

    extra_kwargs = {
        'password': {'write_only': True},
        'is_staff': {'read_only': True},
        'is_admin': {'read_only': True},
    }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context['request']
        Token.objects.get_or_create(user=instance)
        if request.user == instance:
            data['token'] = instance.auth_token.key
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        extra_kwargs = {'email': {"validators": []}, 'password': {'write_only': True}}

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if user is None:
            raise ValidationError('Wrong credentials sent')
        Token.objects.get_or_create(user=User)

        return User

    def get_token(self, obj):
        return obj.auth_token.key
