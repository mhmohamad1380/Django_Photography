from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Blog.views import BlogView, last_blog, blog_detail, PostApiView

urlpatterns = [
    path('blogs', BlogView.as_view()),
    path('blogs/<slug>/<Id>', blog_detail),
    path('last_blog', last_blog, name='last_blog'),
    path('api/blogs', PostApiView.as_view())

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
