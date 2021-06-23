from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from aboutus.views import aboutus

urlpatterns = [
    path('about-us',aboutus)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
