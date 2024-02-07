from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import UserForm
from users.models import User


class LoginView(BaseLogin):
    template_name = "users/login.html"


class LogoutView(BaseLogout):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = "users/register.html"
