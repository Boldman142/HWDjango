from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import index, contact_view, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='catalog'),
    path('contacts/', contact_view, name='contact'),
    path('<int:pk>product/', product, name='product')
]
