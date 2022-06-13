import itertools
from rest_framework import generics
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from Blog.forms import CommentsBlog
from Blog.models import Blog, Comments
from Blog.serializer import PostSerializer


def last_blog(request, *args, **kwargs):
    last_blog: Blog = Blog.object.order_by('-id').all()[:1][0]
    context = {
        'lblog': last_blog
    }
    return render(request, 'last_blog.html', context)


class BlogView(ListView):
    template_name = 'blogs.html'
    paginate_by = 25

    def get_queryset(self):
        return Blog.object.get_active_blogs()


def blog_detail(request, *args, **kwargs):
    comment_form = CommentsBlog(request.POST or None)
    selected_by_id = kwargs['Id']
    selected_blog: Blog = Blog.object.filter(id=selected_by_id).first()
    blog_tags = selected_blog.tags.all()
    related_blogs = Blog.object.filter(category=selected_blog.category.first())[:2]
    filter_comments = Comments.objects.filter(post=selected_blog, publish=True).all()
    if comment_form.is_valid():
        name = comment_form.cleaned_data.get('name')
        phone = comment_form.cleaned_data.get('phone')
        comment = comment_form.cleaned_data.get('comment')
        email = comment_form.cleaned_data.get('email')
        Comments.objects.create(name=name, email=email, comment=comment, phone=phone, post=selected_blog)
        messages.success(request, 'نظر شما با موفقیت ثبت شد و پس از بازبینی منتشر می شود')
        return redirect(f'/blogs/{selected_blog.slug}/{selected_blog.id}')
    comment_form = CommentsBlog()
    context = {
        'sblog': selected_blog,
        'blog_tag': blog_tags,
        'related_blogs': related_blogs,
        'comment_form': comment_form,
        'filter_comments': filter_comments
    }
    return render(request, 'blog_detail.html', context)

class PostApiView(generics.ListAPIView):
    queryset = Blog.object.all()
    serializer_class = PostSerializer