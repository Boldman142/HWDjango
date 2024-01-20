from django.db import models
from django.db.models import SET_NULL, PROTECT

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    overview = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_DEFAULT, default='000')
    price = models.IntegerField(verbose_name='Цена за штуку')
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('date_create',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    overview = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



