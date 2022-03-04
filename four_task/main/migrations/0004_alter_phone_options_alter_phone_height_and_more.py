# Generated by Django 4.0.2 on 2022-03-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_phone_memory_phone_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['pk'], 'verbose_name': 'смартфон', 'verbose_name_plural': 'Смартфоны'},
        ),
        migrations.AlterField(
            model_name='phone',
            name='height',
            field=models.PositiveIntegerField(verbose_name='Высота экрана'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='width',
            field=models.PositiveIntegerField(verbose_name='Ширина экрана'),
        ),
    ]
