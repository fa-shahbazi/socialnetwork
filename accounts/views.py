from rest_framework import generics
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from .permissions import UserOwnerPermission
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


User = get_user_model()


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classs = UserOwnerPermission


    def perfom_create(self, serializer):
        password = serializer.validated_data['password']
        serializer.save(password=make_password(password))


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    permission_classs = UserOwnerPermission
    authentication_classes = TokenAuthentication,

    def perform_update(self, serializer):
        password = serializer.initial_data.get('password')
        if password is not None:
            serializer.save(password=make_password(password))
        else:
            serializer.save()




