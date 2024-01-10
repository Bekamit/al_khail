from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estate', '0001_initial'),
        ('estate', '0002_remove_estate_currency_remove_estate_currency_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_for_purchase', models.BooleanField(default=True, verbose_name='Want to buy')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=70, null=True, verbose_name='Last_name')),
                ('phone', models.CharField(max_length=70, verbose_name='Phone number')),
                ('lang', models.CharField(max_length=30, verbose_name='Message Language')),
                ('at_time', models.DateTimeField(null=True, verbose_name='Call at time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Send date')),
                ('estate_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appel', to='estate.estate')),
            ],
            options={
                'verbose_name': 'Message from site',
                'verbose_name_plural': 'Messages from site',
            },
                ('is_for_purchase', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('lang', models.CharField(max_length=30)),
                ('at_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('estate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appel', to='estate.estate')),
            ],
        ),
    ]
