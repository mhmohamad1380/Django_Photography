# Generated by Django 3.2 on 2021-05-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210501_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=120, null=True, verbose_name='اسم بلاگ در ادرس (فقط انگلیسی)'),
        ),
    ]