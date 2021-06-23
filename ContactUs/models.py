from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=120, blank=False, null=True, verbose_name='نام')
    email = models.EmailField(blank=False, null=True, verbose_name='ایمیل')
    message = models.TextField(blank=False, null=True, verbose_name='پیام')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class About(models.Model):
    phone = models.CharField(max_length=11, blank=False, null=True, verbose_name='شماره تلفن')
    email = models.EmailField(blank=False, null=True, verbose_name='ایمیل')
    address = models.TextField(blank=False, null=True, verbose_name='ادرس')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'اطلاعات'
        verbose_name_plural = 'اطلاعات'
