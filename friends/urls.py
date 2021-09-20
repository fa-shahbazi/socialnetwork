from django.urls import path
from .views import FollowersListAPIView, UnFollowDestroyAPIView

app_name = 'friends'
urlpatterns = [

    path('followers-list/', UnFollowDestroyAPIView.as_view(), name='unfollow'),
    path('followers-list/', FollowersListAPIView.as_view(), name='followers_list'),

]