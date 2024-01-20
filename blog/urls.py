from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogListView, BlogCreateView, BlogDetailView,
                        BlogUpdateView, BlogDeleteView, change_publish)

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('change/<int:pk>/', BlogUpdateView.as_view(), name='blog_change'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post_delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/', change_publish, name='change_publish')
]
