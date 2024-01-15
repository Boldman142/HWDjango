# import json
#
# from django.core.management import BaseCommand
#
from catalog.models import Category, Product
#

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         # Product.objects.all().delete()
#         # Category.objects.all().delete()
#
#         with open('data.json', 'r', encoding='UTF-8') as file:
#             data = json.load(file)
#
#         category = []
#         product = []
#
#         for item in data:
#             if item['model'] == 'catalog.category':
#                 new_category = Category(**item['fields'])
#                 category.append(new_category)
#
#         # Category.object.bulk_create(category)
#         new = Category.objects.all()
#
#         # for i in new:
#         #     print(i.__dict__)
#         for item in data:
#             if item['model'] == 'catalog.product':
#                 pk = item['fields']['category']
#                 item['fields']['category'] = Category.objects.filter(id=pk)
#                 product.append(Product(**item['fields']))
#
#         # for prod in product:
#         #     print(Product.object.get(id))
#
#
#         # Product.object.bulk_create(product)
#
#         # print('python _Xutf8 manage.py dumpdata catalog -o data.json')


import os
from django.core.management import BaseCommand, call_command
from psycopg2 import ProgrammingError, IntegrityError


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
