from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    # Optional: Add any custom logic for login process if required
    # def form_valid(self, form):
    #     return super().form_valid(form)


class UserProfileView(UpdateView):
    model = CustomUser
    form_class = UserChangeForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            if form.data.get('need_generate', False):
                self.object.set_password(
                    self.object.make_random_password(length=12)
                )
                self.object.save()

        return super().form_valid(form)
