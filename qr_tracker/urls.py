# qr_tracker/urls.py
from django.urls import path
from . import views
from .views import IndexView, CommentsView

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('generate_qr/', views.generate_qr, name='generate_qr'),  # API para generar QR
    path('index/', IndexView.as_view(), name='index'),  # Cambiar la ruta para IndexView
    path('comments/', CommentsView.as_view(), name='comments'),  # Añadir comentarios si es necesario
]
