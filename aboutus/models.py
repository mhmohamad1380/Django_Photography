import os
import random

from django.db import models


def get_file_basename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def get_image_path(instance, filename):
    new_name = random.randint(1, 1324328765)
    name, ext = get_file_basename(filename)
    origin_name = f'{new_name}-AboutUs{ext}'
    return f'Gallery/{origin_name}'


# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name='عنوان بالای صفحه')
    subtitle = models.CharField(max_length=120, blank=False, null=True, verbose_name='متن کوتاه زیر عنوان')
    image = models.ImageField(upload_to=get_image_path, blank=False, null=True, verbose_name='تصویر')
    ourstory = models.TextField(max_length=350, blank=False, null=True, verbose_name='داستان ما(حداکثر 350 کارکتر)')
    whatwedo = models.TextField(max_length=350, blank=False, null=True,
                                verbose_name='چه کاری انجام میدیم(حداکثر 350 کارکتر)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'بخش درباره ما'


class OurTeam(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=False, null=True, verbose_name='تصویر عضو')
    name = models.CharField(max_length=120, blank=False, null=True, verbose_name='نام عضو')
    cast = models.CharField(max_length=120, blank=False, null=True, verbose_name='نقش شخص')
    twitter = models.URLField(blank=True, null=True, verbose_name='ادرس توییتر شخض(در صورت تمایل)')
    facebook = models.URLField(blank=True, null=True, verbose_name='ادرس فیس بوک شخص (در صورت تمایل)')
    telegram = models.URLField(blank=True, null=True, verbose_name='ادرس تلگرام شخص(در صورت تمایل)')
    instagram = models.URLField(blank=True, null=True, verbose_name='ادرس اینستاگرام شخص(در صورت تمایل)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تیم ما'
        verbose_name_plural = 'اعضای تیم ما'
