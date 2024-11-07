# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            messages.success(request, f'Tu cuenta ha sido creada. ¡Bienvenido {user.username}!')
            return redirect('base')  # Redirigir a la página de inicio
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
