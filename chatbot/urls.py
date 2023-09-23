from django.urls import path
from . import views

urlpatterns = [
    path('incoming/', views.handle_incoming_messages, name='handle_incoming_messages'),
]
