from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='Company name')),
                ('company_name_en', models.CharField(max_length=50, null=True, verbose_name='Company name')),
                ('company_name_ar', models.CharField(max_length=50, null=True, verbose_name='Company name')),
                ('company_name_tr', models.CharField(max_length=50, null=True, verbose_name='Company name')),
                ('company_name_ru', models.CharField(max_length=50, null=True, verbose_name='Company name')),
                ('about', models.TextField(verbose_name='About company')),
                ('about_en', models.TextField(null=True, verbose_name='About company')),
                ('about_ar', models.TextField(null=True, verbose_name='About company')),
                ('about_tr', models.TextField(null=True, verbose_name='About company')),
                ('about_ru', models.TextField(null=True, verbose_name='About company')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('company_img', models.ImageField(upload_to='company/', verbose_name='Company photo path')),
            ],
            options={
                'verbose_name_plural': 'About company',
            },
                ('company_name', models.CharField(max_length=50)),
                ('company_name_en', models.CharField(max_length=50, null=True)),
                ('company_name_ar', models.CharField(max_length=50, null=True)),
                ('company_name_tr', models.CharField(max_length=50, null=True)),
                ('company_name_ru', models.CharField(max_length=50, null=True)),
                ('about', models.TextField()),
                ('about_en', models.TextField(null=True)),
                ('about_ar', models.TextField(null=True)),
                ('about_tr', models.TextField(null=True)),
                ('about_ru', models.TextField(null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('company_img', models.ImageField(upload_to='company/')),
            ],

        ),
    ]
