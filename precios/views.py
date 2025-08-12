from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from precios.models import Alimento  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

def alimento(request):
    return HttpResponse("Lista de precios está Funcionando")

class Alimentos(ListView):
    model = Alimento
    template_name = "lista_precios.html"
    context_object_name = 'alimentos'

class CrearAlimento(CreateView):
    model = Alimento
    template_name = "crear_alimento.html"
    fields = ['nombre', 'precio', 'unidad', 'descripcion']
    success_url = reverse_lazy('precios:lista_precios')
    
class Ver_alimento(DetailView):
    model = Alimento
    template_name = "ver_alimento.html"

class Actualizar_Alimento(UpdateView):
    model = Alimento
    template_name = "actualizar_alimento.html"
    fields = ['nombre', 'precio', 'unidad', 'descripcion']
    success_url = reverse_lazy('precios:lista_precios')
 
class Eliminar_Alimento(DeleteView):
    model = Alimento
    template_name = "eliminar_alimento.html"
    success_url = reverse_lazy('precios:lista_precios')
