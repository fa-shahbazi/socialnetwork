from django.contrib import admin
from communications.models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('starter',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('starter','room')