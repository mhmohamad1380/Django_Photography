# Generated by Django 3.2 on 2021-05-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20210502_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description2',
            field=models.TextField(null=True, verbose_name='توضیحات2'),
        ),
    ]