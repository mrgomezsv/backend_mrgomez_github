# api_comments/urls.py
from django.urls import path
from .views import create_comment

urlpatterns = [
    path('comments/', create_comment, name='create_comment'),  # Configura la ruta para los comentarios
]
