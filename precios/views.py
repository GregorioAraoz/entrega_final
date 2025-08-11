from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from precios.models import Alimento  
from django.views.generic.edit import CreateView

def alimento(request):
    return HttpResponse("Lista de precios está Funcionando")

class Alimentos(ListView):
    model = Alimento
    template_name = "lista_precios.html"

class CrearAlimento(CreateView):
    model = Alimento
    template_name = "crear_alimento.html"
