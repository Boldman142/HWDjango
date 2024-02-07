from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        user = User.objects.create(
            email='admin@am.min',
            first_name='Admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
