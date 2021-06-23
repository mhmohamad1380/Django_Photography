# Generated by Django 3.2 on 2021-05-02 18:10

import aboutus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True, verbose_name='عنوان بالای صفحه')),
                ('subtitle', models.CharField(max_length=120, null=True, verbose_name='متن کوتاه زیر عنوان')),
                ('image', models.ImageField(null=True, upload_to=aboutus.models.get_image_path, verbose_name='تصویر')),
                ('ourstory', models.TextField(max_length=350, null=True, verbose_name='داستان ما(حداکثر 350 کارکتر)')),
                ('whatwedo', models.TextField(max_length=350, null=True, verbose_name='چه کاری انجام میدیم(حداکثر 350 کارکتر)')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'بخش درباره ما',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=aboutus.models.get_image_path, verbose_name='تصویر عضو')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='نام عضو')),
                ('cast', models.CharField(max_length=120, null=True, verbose_name='نقش شخص')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='ادرس توییتر شخض(در صورت تمایل)')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='ادرس فیس بوک شخص (در صورت تمایل)')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='ادرس تلگرام شخص(در صورت تمایل)')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='ادرس اینستاگرام شخص(در صورت تمایل)')),
            ],
            options={
                'verbose_name': 'تیم ما',
                'verbose_name_plural': 'اعضای تیم ما',
            },
        ),
    ]
