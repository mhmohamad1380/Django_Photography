# Generated by Django 3.2 on 2021-05-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='ایمیل')),
                ('message', models.TextField(null=True, verbose_name='پیام')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
    ]
