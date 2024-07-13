# blog/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_post, name='blog_post'),
    path('blog-post-detail/<str:slug>/', views.blog_detail, name='blog_detail'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
]
