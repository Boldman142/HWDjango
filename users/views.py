from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.conf import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User


class LoginView(BaseLogin):
    template_name = "users/login.html"


class LogoutView(BaseLogout):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = "users/register.html"

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Мои поздравления',
            message='Ты один из нас, бобро пожаловать',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    print(new_password)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
