from django.contrib import admin

# Register your models here.
from aboutus.models import OurTeam, AboutUs

admin.site.register(AboutUs)
admin.site.register(OurTeam)