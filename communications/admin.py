from django.contrib import admin
from communications.models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('starter', 'friend', 'room')

