from django.db import models
from django.db.models import SET_NULL, PROTECT

NULLABLE = {'null': True, 'blank': True}


class Version(models.Model):
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE)
    num_version = models.IntegerField(auto_created=True, verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    sign = models.BooleanField(default=False, verbose_name='В наличии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        unique_together = (('product', 'num_version'),)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    overview = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to='catalog/', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_DEFAULT, default='000')
    price = models.IntegerField(verbose_name='Цена за штуку')
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

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
