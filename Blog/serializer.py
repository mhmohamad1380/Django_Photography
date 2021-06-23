from rest_framework import serializers

from Blog.models import Blog


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'image', 'date', 'author', 'description', 'tags', 'active']
