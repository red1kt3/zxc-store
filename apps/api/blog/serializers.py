from rest_framework import serializers

from apps.blog.models import BlogCategory, Article
from apps.user.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image'
        )





class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
        )

