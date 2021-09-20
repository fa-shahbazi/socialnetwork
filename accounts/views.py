from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from accounts.serializers import UserLoginSerializer, UserSerializer, ProfileSerializer
from .accounts_backend import generate_verification_code

User = get_user_model()


class RegisterUser(generics.CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        cache.set('username', username, timeout=100)
        cache.set('password', password, timeout=100)
        cache.set('email', email, timeout=100)
        code = generate_verification_code()
        cache.set('code', 'code', timeout=100)
        print(code)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'result': 'The activation code was sent!'}, status=status.HTTP_200_OK)


class RegisterUserConfirm(generics.CreateAPIView):
    permission_classes = AllowAny,
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        username = cache.get('username')
        password = cache.get('password')
        email = cache.get('email')
        if not all([username, password]):
            return Response({'result': 'The code Was Expired!'})
        data = {'username': username, 'password': password}
        if email is not None:
            data['email'] = email
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        Token.objects.get_or_create(user=instance)
        headers = self.get_success_headers(serializer.data)
        return Response({'result': 'Account Was created!'}, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny, ]



