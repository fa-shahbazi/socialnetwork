from communications.models import Message, Room
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    starter = serializers.SerializerMethodField(read_only=True, required=False)
    friend = serializers.CharField(write_only=True, required=False)
    goal = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = Message
        fields = ['from_user', 'to_user', 'message', 'goal', 'room']

    def create(self, validated_data):
        request = self.context.get('request')
        friend = User.objects.get(username=validated_data.pop('friend'))
        instance = Message.objects.create(starter=request.user, friend=friend, **validated_data)
        return instance

    def get_goal(self, obj):
        return obj.friend.username

    def get_starter(self, obj):
        return obj.starter.username


