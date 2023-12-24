from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryADMIN(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


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
    inlines = [ProductCategoryInLine, ImageInline]
    list_display_links = ['id', 'name', 'price', 'quantity']





