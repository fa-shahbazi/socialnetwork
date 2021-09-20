from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from friends.serializers import RelationSerializer
from friends.models import Relation
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
User = get_user_model()


class FollowersListAPIView(generics.ListCreateAPIView):
    serializer_class = RelationSerializer
    queryset = Relation.objects.all()

    def perform_create(self, serializer):
        following = User.objects.filter(username=serializer.validated_data.get('from_user'))[0]
        instance = Relation.objects.create(from_user=self.request.user, to_user=following)
        return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {'username': instance.following.username}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class UnFollowDestroyAPIView(generics.DestroyAPIView):
    serializer_class = RelationSerializer
    queryset = Relation.objects.all()

    def get_object(self):
        return Relation.objects.filter(from_user=self.request.user, following__username=self.request.data.get('from_user')).first()


