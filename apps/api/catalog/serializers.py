from rest_framework import serializers

from apps.catalog.models import Category, Product, Image


class CategoryReadSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True)


    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'slug',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )



class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
        )


class ProductReadSerializer(serializers.ModelSerializer):
    categories = CategoryReadSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'categories',
        )





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'parent',
            'description',
            'image',
        )




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image',
            'product',
            'is_main',

        )

