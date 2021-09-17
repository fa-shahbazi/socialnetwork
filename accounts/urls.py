from django.urls import path
from accounts.views import RegisterView, UserListCreateAPIView, UserRetrieveUpdateDestroy

app_name = 'accounts'
urlpatterns = [
    # api views
    path('register-view/', RegisterView.as_view(), name='register_view'),
    path('login-view/', UserListCreateAPIView.as_view(), name='login_view'),
    path('user-api/<str:username>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),

]