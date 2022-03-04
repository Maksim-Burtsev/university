from pyexpat import model
from statistics import mode
from django.db import models


class Triangle(models.Model):

    first_side = models.IntegerField('Первая строна')
    second_side = models.IntegerField('Вторая строна')
    third_side = models.IntegerField('Третья строна')

    area = models.DecimalField('Площадь', max_digits=17, decimal_places=2)

    class Meta:
        verbose_name = 'сторона'
        verbose_name = 'Стороны'