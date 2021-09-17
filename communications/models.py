from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models
import uuid

User = get_user_model()


class Room(models.Model):
    id = models.UUIDField(verbose_name=_('id'), default=uuid.uuid4,
                          primary_key=True, editable=False)
    starter = models.ForeignKey(User, verbose_name=_('starter'),
                                related_name='starter_room', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, verbose_name=_('friend'),
                               related_name='friend_room', on_delete=models.CASCADE)


class Message(models.Model):
    starter = models.ForeignKey(User, verbose_name=_('starter'),
                                related_name='starter_messages', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, verbose_name=_('friend'),
                               related_name='friend_messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name=_('room'),
                             related_name='messages', on_delete=models.DO_NOTHING)
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.message + " " + str(self.created_at)


