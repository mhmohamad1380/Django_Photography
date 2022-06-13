from django.shortcuts import render
from django.views.generic import ListView

from Blog.models import Blog
from Gallery.models import GalleryModel


def homepage(request, *args, **kwargs):
    last_blogs: Blog = Blog.object.order_by('-id').all()[:3]
    context = {
        'lblogs': last_blogs

    }
    return render(request, 'Homepage.html', context)


def error_handler_404(request, exception):
    return render(request, '404_page.html', {})
