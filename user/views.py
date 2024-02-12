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
from django.views.generic import CreateView, UpdateView
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


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('main:product-list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('main:product-list')


class PasswordResetView(View):
    template_name = 'registration/password_form.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_user_model().objects.get(email=email)
            password = get_user_model().objects.make_random_password()
            user.set_password(password)
            user.save()

            subject = 'Пароль изменен'
            message = 'Ваш новый пароль: {password}'.format(password=password)

            from_email = user.email
            send_mail(subject, message, from_email, [user.email])

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return HttpResponseRedirect(reverse('password_reset_done'))
        return render(request, self.template_name, {'form': form})


@login_required
class UserPasswordResetDoneView(PasswordResetDoneView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/send_password.html'
    success_url = reverse_lazy('user:password_reset_done')


@login_required
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/confirm_password.html'
    success_url = reverse_lazy('user:password_reset_confirm')


@login_required
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('user:password_reset_done')
