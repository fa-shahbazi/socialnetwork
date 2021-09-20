from django.urls import path
from .views import MessageListApiView

app_name = 'communications'
urlpatterns = [
    path('messagelist/', MessageListApiView.as_view(), name='message_list'),
]