from django.contrib import admin

# Register your models here.
from ContactUs.models import ContactUs, About

admin.site.register(ContactUs)
admin.site.register(About)
