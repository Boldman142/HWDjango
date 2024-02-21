from config import settings
from django.core.cache import cache
from catalog.models import Category, Product


def get_prod_categories_cache(category):
    if settings.CACHE_ENABLED:
        key = f'product_list_{category}'
        queryset = cache.get(key)
        if queryset is None:
            queryset = Product.objects.all()
            queryset = queryset.filter(category=category)
            cache.set(key, queryset)
    else:
        queryset = Product.objects.all()
        queryset = queryset.filter(category=category)
    return queryset


def get_categories_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
