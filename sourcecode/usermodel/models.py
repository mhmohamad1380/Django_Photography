from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    sexuality = models.CharField(max_length=20,blank=False,null=True,verbose_name='جنسیت')
