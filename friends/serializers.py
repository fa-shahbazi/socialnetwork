from friends.models import Relation
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from accounts.serializers import UserSerializer


class RelationSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = serializers.CharField(write_only=True)

    class Meta:
        model = Relation
        fields = ['from_user', 'to_user']
        read_only_fields = ['from_user',]

