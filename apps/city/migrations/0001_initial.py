# Generated by Django 4.2.8 on 2024-02-02 17:59

import apps.city.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255, unique=True, verbose_name='City')),
                ('city_name_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='City')),
                ('city_name_ar', models.CharField(max_length=255, null=True, unique=True, verbose_name='City')),
                ('city_name_tr', models.CharField(max_length=255, null=True, unique=True, verbose_name='City')),
                ('city_name_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='City')),
                ('city_description', models.TextField(verbose_name='City descriptions')),
                ('city_description_en', models.TextField(null=True, verbose_name='City descriptions')),
                ('city_description_ar', models.TextField(null=True, verbose_name='City descriptions')),
                ('city_description_tr', models.TextField(null=True, verbose_name='City descriptions')),
                ('city_description_ru', models.TextField(null=True, verbose_name='City descriptions')),
                ('city_img', models.ImageField(upload_to=apps.city.models.City.upload_to, verbose_name='City photo path')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
