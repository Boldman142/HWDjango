from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, contact_view, ProductListView, ProductDetailView,
                           ProductCreateView, BlogListView, BlogCreateView, BlogDetailView,
                           BlogUpdateView, BlogDeleteView, change_publish)

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='catalog'),
    path('contacts/', contact_view, name='contact'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category'),
    path('product_detail_<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/change/<int:pk>/', BlogUpdateView.as_view(), name='blog_change'),
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('blog/post_delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
    path('blog/<int:pk>/', change_publish, name='change_publish')
]
