from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('generate_qr/', views.generate_qr, name='generate_qr'),  # API para generar QR
]
