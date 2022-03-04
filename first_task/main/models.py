from django.db import models


class Category(models.Model):

    basis = models.IntegerField('Число')


class Numbers(models.Model):

    first_num = models.IntegerField('Первое число')
    secont_num = models.IntegerField('Второе число')

    res_multiply = models.IntegerField('Результат умножения')

    cat = models.ForeignKey(Category,
                            on_delete=models.CASCADE, 
                            related_name='nums'
                            )

    class Meta:
        verbose_name = 'число'
        verbose_name_plural = 'Числа'
