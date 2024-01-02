from django.urls import path

from catalog.views import index, contact_view

app_name = 'catalog'

urlpatterns = [
    path('', index, name='catalog'),
    path('', contact_view, name='contact')
]
