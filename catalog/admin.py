from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'num_version', 'name', 'sign')
    list_filter = ('product',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'overview')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
