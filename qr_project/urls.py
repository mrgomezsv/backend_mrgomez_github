"""
URL configuration for qr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# /backend_mrgomez_github/qr_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from qr_tracker.views import IndexView, CommentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('qr/', include('qr_tracker.urls')),  # Incluye las URLs de qr_tracker
    path('accounts/', include('accounts.urls')),  # Añadir autenticación
    path('api/', include('api_comments.urls')),
    path('comments/', CommentsView.as_view(), name='comments'),

    # Redirigir la raíz '/' al login
    path('', lambda request: HttpResponseRedirect('/accounts/login/')),
]
