# Generated by Django 3.2 on 2021-05-01 18:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='active',
            field=models.BooleanField(default=False, verbose_name='تایید شده / نشده'),
        ),
    ]
