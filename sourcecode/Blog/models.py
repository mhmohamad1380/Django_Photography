import os
import random

from django.db import models
from django.utils import timezone

from extensions.utils import jalali_datetime, jalali_date, jalali_date_without_day
from usermodel.models import User


class BlogManager(models.Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(active=True)


def get_file_basename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def get_image_path(instance, filename):
    new_name = random.randint(1, 1324328765)
    name, ext = get_file_basename(filename)
    origin_name = f'{new_name}-Blog{ext}'
    return f'Gallery/{origin_name}'


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name='عنوان دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Tag(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name='عنوان تگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, verbose_name='عنوان بلاگ')
    slug = models.SlugField(max_length=120, blank=False, null=True, verbose_name='اسم بلاگ در ادرس (فقط انگلیسی)')
    category = models.ManyToManyField(Category, blank=False, verbose_name='دسته بندی')
    image = models.ImageField(upload_to=get_image_path, blank=False, null=True, verbose_name='تصویر بلاگ')
    image2 = models.ImageField(upload_to=get_image_path, blank=True, null=True, verbose_name='تصویر بلاگ2')
    image3 = models.ImageField(upload_to=get_image_path, blank=True, null=True, verbose_name='تصویر بلاگ3')
    image4 = models.ImageField(upload_to=get_image_path, blank=True, null=True, verbose_name='تصویر بلاگ4')
    image5 = models.ImageField(upload_to=get_image_path, blank=True, null=True, verbose_name='تصویر بلاگ5')
    date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ نوشتن خبر')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, verbose_name='نویسنده')
    description = models.TextField(blank=False, null=True, verbose_name='توضیحات')
    description2 = models.TextField(blank=False, null=True, verbose_name='توضیحات2')
    tags = models.ManyToManyField(Tag, blank=False, verbose_name='تگ ها')
    active = models.BooleanField(default=False, verbose_name='تایید شده / نشده')

    object = BlogManager()

    def __str__(self):
        return self.title

    def jtdate(self):
        return jalali_datetime(self.date)

    def jdate(self):
        return jalali_date_without_day(self.date)

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'
        ordering = ['-date']


class Comments(models.Model):
    name = models.CharField(max_length=120, blank=False, null=True, verbose_name='نام نظر دهنده')
    phone = models.CharField(max_length=20, blank=False, null=True, verbose_name='شماره نظر دهنده')
    email = models.EmailField(blank=False, null=True, verbose_name='ایمیل نظر دهنده')
    comment = models.TextField(blank=False, null=True, verbose_name='نظر')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=False, null=True, verbose_name='پست')
    publish = models.BooleanField(default=False, verbose_name='منتشر شود / نشود')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
