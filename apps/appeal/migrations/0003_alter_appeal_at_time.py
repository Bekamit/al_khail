# Generated by Django 4.2.8 on 2023-12-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0002_alter_appeal_options_alter_appeal_at_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='at_time',
            field=models.DateTimeField(blank=True, verbose_name='Call at time'),
        ),
    ]
