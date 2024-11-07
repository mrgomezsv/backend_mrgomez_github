# qr_tracker/urls.py
from django.urls import path
from .views import IndexView, CommentsView, base

urlpatterns = [
    path('', base, name='base'),  # URL para la vista 'home'
    path('comments/', CommentsView.as_view(), name='comments'),
]