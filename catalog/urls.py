from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from catalog.views import index, contact_view

app_name = 'catalog'

urlpatterns = [
    path('', index, name='catalog'),
    path('', contact_view, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
