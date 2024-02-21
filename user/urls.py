from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import path

from user.apps import UserConfig
from user.views import (RegisterView, CustomLogoutView, UserPasswordResetDoneView, UserPasswordResetConfirmView,
                        UserPasswordResetCompleteView, UserPasswordResetView)

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('accounts/', include('django.urls')),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
