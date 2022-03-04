from django.db import models
from django.urls import reverse


class Phone(models.Model):
    """Модель смартфона"""

    producer = models.CharField('Производитель', max_length=255)
    model = models.CharField('Модель', max_length=255)
    photo_link = models.CharField('Ссылка на фото', max_length=255)
    width = models.PositiveIntegerField('Ширина экрана')
    height = models.PositiveIntegerField('Высота экрана')
    memory = models.PositiveIntegerField('Объём памяти')
    price = models.PositiveIntegerField('Цена')

    def __str__(self) -> str:
        return f'{self.producer.capitalize()} {self.model}'

    def get_absolute_url(self):
        return reverse('edit', kwargs={'post_pk' : self.pk})


    class Meta:
        verbose_name = 'смартфон'
        verbose_name_plural = 'Смартфоны'
        ordering = ['-pk',]