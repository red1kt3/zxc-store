from rest_framework import serializers

from apps.blog.models import BlogCategory, Article, Tag
from apps.user.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = (
            'id',
            'name',
            'image'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'tags'
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True)

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
            'tags',
        )






class ArticleWriteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=64))

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
            'tags',

        )

