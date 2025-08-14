from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            
            django_login(request, user)
            return redirect('app_inicial:inicio')
            
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
    else:
        formulario = FormularioRegistro()
    
    return render(request, 'registro.html', {'formulario': formulario})