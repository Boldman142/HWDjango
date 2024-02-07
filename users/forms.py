from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleForMixin
from users.models import User


class UserForm(StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

