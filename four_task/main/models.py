from tabnanny import verbose
from django.db import models


class Phone(models.Model):
    """Модель смартфона"""

    producer = models.CharField('Производитель', max_length=255)
    model = models.CharField('Модель', max_length=255)
    photo_link = models.CharField('Ссылка на фото', max_length=255)
    width = models.PositiveIntegerField('Ширина')
    height = models.PositiveIntegerField('Высота')
    memory = models.PositiveIntegerField('Объём памяти')
    price = models.PositiveIntegerField('Цена')

    def __str__(self) -> str:
        return f'{self.producer.capitalize()} {self.model}'

    class Meta:
        verbose_name = 'смартфон'
        verbose_name_plural = 'Смартфоны'

