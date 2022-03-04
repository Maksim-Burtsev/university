from django.db import models

class Product(models.Model):

    name = models.CharField('Продукт', max_length=250)
    price = models.IntegerField('Цена')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
