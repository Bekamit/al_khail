# Generated by Django 4.2.8 on 2024-02-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogDownloader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='Phone number')),
                ('role', models.CharField(max_length=30, verbose_name='Role')),
                ('lang', models.CharField(blank=True, max_length=30, verbose_name='Respondent language')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog', to='estate.estate', verbose_name='Estate interest')),
            ],
            options={
                'verbose_name': 'Catalog downloader',
                'verbose_name_plural': 'Catalog downloaders',
            },
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeal_type', models.CharField(choices=[('buy', 'buy'), ('sell', 'sell'), ('consultation', 'consultation')], default=('consultation', 'consultation'), max_length=125, verbose_name='Type of appeal')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('phone', models.CharField(max_length=70, verbose_name='Phone number')),
                ('date', models.DateField(verbose_name='date of call back')),
                ('lang', models.CharField(blank=True, max_length=30, verbose_name='Message Language')),
                ('city', models.CharField(max_length=100, verbose_name='Respondent city')),
                ('at_date', models.DateField(null=True, verbose_name='Call in date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Send date')),
                ('is_send', models.BooleanField(default=True, verbose_name='Send letter')),
                ('estate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appeals', to='estate.estate')),
            ],
            options={
                'verbose_name': 'Message from site',
                'verbose_name_plural': 'Messages from site',
            },
        ),
    ]
