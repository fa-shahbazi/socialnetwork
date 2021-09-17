from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User


class UserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user is None:
            return
        if user.check_password(password):
            return user