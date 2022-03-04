# Generated by Django 4.0.2 on 2022-03-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'смартфон',
                'verbose_name_plural': 'Смартфоны',
            },
        ),
    ]
