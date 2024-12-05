from django.urls import path
from . import views
from .views import (
    post_list, post_detail, post_create, post_edit, post_delete,
    PostListAPI, PostDetailAPI
)

urlpatterns = [
    # Web Views
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    # API Views
    path('api/posts/', PostListAPI.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', PostDetailAPI.as_view(), name='post_detail_api'),
]
