from django.urls import path
from core.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('login', UsernamePasswordLoginView.as_view(), name='username_password_login_view'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh_token_view'),
    path('verify-token', TokenVerifyView.as_view(), name='verify_token_view'),
    path('logout', TokenBlacklistView.as_view(), name='logout'),
]