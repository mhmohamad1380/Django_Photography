# Generated by Django 3.2 on 2021-05-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='Blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='Blog.Tag', verbose_name='تگ ها'),
        ),
    ]
