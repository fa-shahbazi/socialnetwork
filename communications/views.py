from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from communications.serializers import MessageSerializer
from communications.models import Message


class MessageListApiView(ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(friend=self.request.user)


