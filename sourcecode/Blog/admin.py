from django.contrib import admin

# Register your models here.
from Blog.models import Tag, Blog, Category, Comments


class CommentSetting(admin.ModelAdmin):
    list_display = ['__str__', 'comment', 'publish']
    list_editable = ['publish']


class BlogSetting(admin.ModelAdmin):
    list_display = ['__str__', 'id','active']
    list_editable = ['active']


admin.site.register(Tag)
admin.site.register(Blog, BlogSetting)
admin.site.register(Category)
admin.site.register(Comments, CommentSetting)
