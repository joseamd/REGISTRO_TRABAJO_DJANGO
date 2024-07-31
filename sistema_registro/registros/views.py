from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroTrabajoForm, RegistroUsuarioForm
from .models import RegistroTrabajo
from django.contrib.auth.models import User

@login_required
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroTrabajoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('listar_registros')
    else:
        form = RegistroTrabajoForm()
    return render(request, 'registros/crear_registro.html', {'form': form})

@login_required
def listar_registros(request):
    registros = RegistroTrabajo.objects.filter(usuario=request.user)
    return render(request, 'registros/listar_registros.html', {'registros': registros})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_registros')  # Redirige a la página de registros después de registrarse
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registros/registro.html', {'form': form})
