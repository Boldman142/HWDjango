from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    message = models.TextField(verbose_name='Сообщение')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True)
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.name}: {self.date_create} '

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
