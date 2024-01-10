from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_image', models.ImageField(upload_to='default_image/', verbose_name='default image path')),
                ('field1', models.CharField(max_length=100)),
                ('field1_en', models.CharField(max_length=100, null=True)),
                ('field1_ar', models.CharField(max_length=100, null=True)),
                ('field1_tr', models.CharField(max_length=100, null=True)),
                ('field1_ru', models.CharField(max_length=100, null=True)),
                ('field2', models.TextField()),
                ('field2_en', models.TextField(null=True)),
                ('field2_ar', models.TextField(null=True)),
                ('field2_tr', models.TextField(null=True)),
                ('field2_ru', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Static Data',
                'verbose_name_plural': 'Static Data',
            },
        ),
    ]
