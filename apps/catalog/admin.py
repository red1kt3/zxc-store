from django.contrib import admin
from apps.catalog.models import Category, Product


@admin.register(Category)
class CategoryADMIN(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity']
    list_display_links = ['id', 'name', 'price', 'quantity']

