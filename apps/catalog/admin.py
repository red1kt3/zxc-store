from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ['image_tag']
    fields = ['name', 'slug', 'parent', 'description', 'image_tag', 'image', 'meta_title', 'meta_description',
              'meta_keywords' ]


class ProductCategoryInLine(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['product', 'image_tag', 'image', 'is_main']
    readonly_fields = ['image_tag']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity',]
    fields = ['name', 'description', 'price', 'quantity', 'meta_title', 'meta_description', 'meta_keywords']
    inlines = [ProductCategoryInLine, ImageInline]
    list_display_links = ['id', 'name', 'price', 'quantity']





