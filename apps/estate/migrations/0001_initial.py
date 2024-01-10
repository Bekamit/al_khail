
# Generated by Django 4.2.8 on 2024-01-10 12:39

import apps.estate.models
from django.db import migrations, models
import django.db.models.deletion

# Generated by Django 4.2.8 on 2023-12-21 13:37

from django.db import migrations, models
import django.db.models.deletion
import apps.estate.models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='estate_name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='estate_name')),
                ('name_ar', models.CharField(max_length=100, null=True, verbose_name='estate_name')),
                ('name_tr', models.CharField(max_length=100, null=True, verbose_name='estate_name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='estate_name')),

                ('developer', models.CharField(max_length=100, verbose_name='Developer')),
                ('developer_en', models.CharField(max_length=100, null=True, verbose_name='Developer')),
                ('developer_ar', models.CharField(max_length=100, null=True, verbose_name='Developer')),
                ('developer_tr', models.CharField(max_length=100, null=True, verbose_name='Developer')),
                ('developer_ru', models.CharField(max_length=100, null=True, verbose_name='Developer')),
                ('area', models.FloatField(verbose_name='estate_area')),
                ('district', models.CharField(max_length=100, verbose_name='District')),
                ('district_en', models.CharField(max_length=100, null=True, verbose_name='District')),
                ('district_ar', models.CharField(max_length=100, null=True, verbose_name='District')),
                ('district_tr', models.CharField(max_length=100, null=True, verbose_name='District')),
                ('district_ru', models.CharField(max_length=100, null=True, verbose_name='District')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('description_en', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('description_ar', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('description_tr', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('is_secondary', models.BooleanField(default=True, verbose_name='Secondary estate')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),

                ('developer', models.CharField(max_length=100, verbose_name='estate_developer')),
                ('developer_en', models.CharField(max_length=100, null=True, verbose_name='estate_developer')),
                ('developer_ar', models.CharField(max_length=100, null=True, verbose_name='estate_developer')),
                ('developer_tr', models.CharField(max_length=100, null=True, verbose_name='estate_developer')),
                ('developer_ru', models.CharField(max_length=100, null=True, verbose_name='estate_developer')),
                ('area', models.FloatField(verbose_name='estate_area')),
                ('district', models.CharField(max_length=100, verbose_name='estate_district')),
                ('district_en', models.CharField(max_length=100, null=True, verbose_name='estate_district')),
                ('district_ar', models.CharField(max_length=100, null=True, verbose_name='estate_district')),
                ('district_tr', models.CharField(max_length=100, null=True, verbose_name='estate_district')),
                ('district_ru', models.CharField(max_length=100, null=True, verbose_name='estate_district')),
                ('description', models.TextField(max_length=500, verbose_name='estate_description')),
                ('description_en', models.TextField(max_length=500, null=True, verbose_name='estate_description')),
                ('description_ar', models.TextField(max_length=500, null=True, verbose_name='estate_description')),
                ('description_tr', models.TextField(max_length=500, null=True, verbose_name='estate_description')),
                ('description_ru', models.TextField(max_length=500, null=True, verbose_name='estate_description')),
                ('is_secondary', models.BooleanField(default=True, verbose_name='estate_is_secondary')),
                ('price', models.FloatField()),
                ('price_en', models.FloatField(null=True)),
                ('price_ar', models.FloatField(null=True)),
                ('price_tr', models.FloatField(null=True)),
                ('price_ru', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=4)),
                ('currency_en', models.CharField(max_length=4, null=True)),
                ('currency_ar', models.CharField(max_length=4, null=True)),
                ('currency_tr', models.CharField(max_length=4, null=True)),
                ('currency_ru', models.CharField(max_length=4, null=True)),
                ('pdf_cataloge', models.FileField(upload_to=apps.estate.models.Estate.upload_to)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('vizits', models.IntegerField(default=1)),

                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='estate', to='city.city')),
            ],
        ),
        migrations.CreateModel(
            name='EstateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('type', models.CharField(max_length=30, verbose_name='Estate Type')),
                ('type_en', models.CharField(max_length=30, null=True, verbose_name='Estate Type')),
                ('type_ar', models.CharField(max_length=30, null=True, verbose_name='Estate Type')),
                ('type_tr', models.CharField(max_length=30, null=True, verbose_name='Estate Type')),
                ('type_ru', models.CharField(max_length=30, null=True, verbose_name='Estate Type')),
            ],
            options={
                'verbose_name': 'Estate Type',
                'verbose_name_plural': 'Estate Types',
            },

                ('type', models.CharField(max_length=30)),
                ('type_en', models.CharField(max_length=30, null=True)),
                ('type_ar', models.CharField(max_length=30, null=True)),
                ('type_tr', models.CharField(max_length=30, null=True)),
                ('type_ru', models.CharField(max_length=30, null=True)),
            ],

        ),
        migrations.CreateModel(
            name='EstateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=apps.estate.models.EstateImage.upload_to)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='estate.estate')),
            ],
        ),
        migrations.AddField(
            model_name='estate',
            name='estate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='estate', to='estate.estatetype'),
        ),
    ]
