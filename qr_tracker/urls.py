# qr_tracker/urls.py
from django.urls import path
from .views import IndexView, CommentsView, home

urlpatterns = [
    path('', home, name='home'),  # URL para la vista 'home'
    path('index/', IndexView.as_view(), name='index'),  # URL para la vista 'index'
    path('comments/', CommentsView.as_view(), name='comments'),  # URL para la vista 'comments'
]
