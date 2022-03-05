from tabnanny import verbose
from django.db import models


class Team(models.Model):
    """Модель команды"""

    name = models.CharField('Название команды', max_length=255)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'Команды'


class Player(models.Model):
    """Модель игрока"""

    name = models.CharField('Имя игрока', max_length=255)
    number = models.PositiveIntegerField('Номер')
    team = models.ForeignKey(Team,
                             verbose_name='Команда',
                             on_delete=models.CASCADE, 
                             related_name='players')
    photo = models.CharField('Фото', max_length=255, blank=True)
    wiki_link = models.CharField('Ссылка на Википедию', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['-pk', ]
