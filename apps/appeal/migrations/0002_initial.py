# Generated by Django 4.2.8 on 2024-01-12 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appeal', '0001_initial'),
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='estate_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appel', to='estate.estate'),
        ),
    ]