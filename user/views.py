from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView, FormView
from .forms import CustomUserCreationForm, UserChangeForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return response


# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#     redirect_authenticated_user = False
#
#     def get_success_url(self):
#         return reverse_lazy('main:product-list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main:product-list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserPasswordResetView(FormView):
    template_name = 'registration/password_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('user:password_reset_done')

    def form_valid(self, form):
        form.save(request=self.request)
        return super().form_valid(form)


class UserPasswordResetDoneView(PasswordResetDoneView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/send_password.html'
    success_url = reverse_lazy('user:password_reset_done')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/confirm_password.html'
    success_url = reverse_lazy('password_reset_confirm')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_reset_done')
