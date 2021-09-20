from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login-view/', views.UserLoginAPIView.as_view(), name='login_view'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('confirm-register/', views.RegisterUserConfirm.as_view(), name='confirm_register'),
]
