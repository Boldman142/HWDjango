from catalog.models import Category, Product

import os
from django.core.management import BaseCommand, call_command
from psycopg2 import ProgrammingError, IntegrityError


# python manage.py dumpdatautf8 catalog --output data.json

class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()
        path = os.path.join('data.json')

        try:
            call_command('loaddata', path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write('OK', self.style.SUCCESS)
