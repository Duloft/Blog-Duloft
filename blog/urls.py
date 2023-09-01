# blog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_post, name='blog_post'),
    path('blog-post-detail/<str:slug>/', views.blog_detail, name='blog_post_detail'),
]
