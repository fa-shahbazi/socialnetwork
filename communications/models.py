from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models
import uuid

User = get_user_model()


class Room(models.Model):
    id = models.UUIDField(verbose_name=_('id'), default=uuid.uuid4, primary_key=True, editable=False)
    sender = models.ForeignKey(User, verbose_name=_('sender'),
                                related_name='start_rooms', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, verbose_name=_('reciever'),
                               related_name='end_rooms', on_delete=models.CASCADE)

    class Meta:
        db_table = 'rooms'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    def __str__(self):
        return f'{self.sender.username} - {self.reciever.username}'


class Message(models.Model):
    starter = models.ForeignKey(User, verbose_name=_('starter'),
                                related_name='starter', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, verbose_name=_('friend'),
                               related_name='friend', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name=_('room'),
                             related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('updated at'))

    def __str__(self):
        return self.sender.username + " " + str(self.created_at)

    class Meta:
        db_table = 'messages'
        verbose_name = _('message')
        verbose_name_plural = _('messages')


