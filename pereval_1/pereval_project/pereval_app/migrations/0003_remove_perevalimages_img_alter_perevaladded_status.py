# Generated by Django 4.1.7 on 2023-04-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval_app', '0002_coord_level_perevaladded_perevalimages_perevaluser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perevalimages',
            name='img',
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('new', 'Новая заявка'), ('pending', 'Модератор взял в работу'), ('accepted', 'Модерация прошла успешно'), ('rejected', 'Модерация прошла, информация не принята')], default='new', max_length=10),
        ),
    ]
