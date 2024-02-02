# Generated by Django 4.2.8 on 2024-02-02 17:59

import apps.estate.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_tr', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('area', models.FloatField(verbose_name='Area (m²)')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('description_en', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('description_ar', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('description_tr', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('price_usd', models.FloatField(verbose_name='Price at ($)')),
                ('is_secondary', models.BooleanField(default=False, verbose_name='Secondary estate')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('visits', models.IntegerField(default=0, verbose_name='Visits')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='estate', to='city.city')),
            ],
            options={
                'verbose_name': 'Estate',
                'verbose_name_plural': 'Estates',
                'ordering': ['price_usd'],
            },
        ),
        migrations.CreateModel(
            name='EstateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30, unique=True, verbose_name='Estate Type')),
                ('type_en', models.CharField(max_length=30, null=True, unique=True, verbose_name='Estate Type')),
                ('type_ar', models.CharField(max_length=30, null=True, unique=True, verbose_name='Estate Type')),
                ('type_tr', models.CharField(max_length=30, null=True, unique=True, verbose_name='Estate Type')),
                ('type_ru', models.CharField(max_length=30, null=True, unique=True, verbose_name='Estate Type')),
            ],
            options={
                'verbose_name': 'Estate Type',
                'verbose_name_plural': 'Estate Types',
            },
        ),
        migrations.CreateModel(
            name='EstateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=apps.estate.models.EstateImage.upload_to)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='estate.estate')),
            ],
        ),
        migrations.AddField(
            model_name='estate',
            name='estate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='estate', to='estate.estatetype'),
        ),
        migrations.AddField(
            model_name='estate',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estate', to='project.project', verbose_name='Project'),
        ),
    ]
