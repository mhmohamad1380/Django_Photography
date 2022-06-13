from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from usermodel.models import User
UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email','sexuality')
UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','sexuality')
admin.site.register(User, UserAdmin)
