from django.db import models

# Create your models here.
import os
import random


class Gallery_Manager(models.Manager):
    def get_active_images(self):
        return self.get_queryset().filter(active=True)


def get_file_basename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def get_image_path(instance, filename):
    new_name = random.randint(1, 1324328765)
    name, ext = get_file_basename(filename)
    origin_name = f'{new_name}-Gallery{ext}'
    return f'Gallery/{origin_name}'


class GalleryModel(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name='عنوان تصویر')
    short_description = models.TextField(blank=True, null=True, verbose_name='توضیح خیلی کوتاه')
    image = models.ImageField(upload_to=get_image_path, blank=False, null=True)
    active = models.BooleanField(blank=False, default=False, verbose_name='نمایش داده شود / نشود')

    object = Gallery_Manager()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'تصاویر'
