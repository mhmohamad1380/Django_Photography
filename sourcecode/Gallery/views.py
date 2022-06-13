from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from Gallery.models import GalleryModel


class GalleryView(ListView):
    template_name = 'gallery.html'
    paginate_by = 30

    def get_queryset(self):
        return GalleryModel.object.get_active_images()
