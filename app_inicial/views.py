from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from app_inicial.models import Animal
from app_inicial.forms import formularioanimal,formulariobusqueda,formularioactualizar

def app_inicial(request):
    return render(request, 'main_template.html')

def saludo(request):
    fecha = datetime.now()
    return HttpResponse(f')<h1>{fecha.strftime('%H:%M:%S')}: Hola </h1>')

def saludo_template(request, nombre, apellido):
    
    archivo_abierto = open(r'C:/Proyecto_Coder_Django/django_entrega/templates/saludo_template.html')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    fecha = datetime.now()
    
    datos = {
        'fecha' : fecha.strftime('%H:%M:%S'),
        'nombre' : nombre,
        'apellido' : apellido
        
    }
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)


def saludo_con_cargador(request, nombre, apellido):
    
    # archivo_abierto = open(r'C:/Proyecto_Coder_Django/django_entrega/templates/saludo_template.html')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    
    fecha = datetime.now()
    
    datos = {
        'fecha' : fecha.strftime('%H:%M:%S'),
        'nombre' : nombre,
        'apellido' : apellido
        
    }
    
    template = loader.get_template(r'saludo_template.html')
    
    # contexto = Context()
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

########################################################3333

def saludo_con_render(request, nombre, apellido):
    
    # archivo_abierto = open(r'C:/Proyecto_Coder_Django/django_entrega/templates/saludo_template.html')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    
    fecha = datetime.now()
    
    datos = {
        'fecha' : fecha.strftime('%H:%M:%S'),
        'nombre' : nombre,
        'apellido' : apellido
        
    }
    
    # template = loader.get_template(r'saludo_template.html')
    
    # template_renderizado = template.render(datos)
    
    # return HttpResponse(template_renderizado)
    
    return render(request, 'saludo_template.html', datos)

#########################################################

def condicion_y_bucle(request):
    return render(request, 'condicion_y_bucle.html', {
        "listado_de_numeros": [1, 2, 3, 4, 5, 6]
    })
    
    
def crear_animales(request):
    if request.method == 'POST':
        formulario = formularioanimal(request.POST)
        if formulario.is_valid():
            nueva_data = formulario.cleaned_data
            animal = Animal(especie=nueva_data['especie'], alimentacion=nueva_data['alimentacion'])
            animal.save()
            return render(request, 'animal_creado.html', {'animal': animal})
    else:
        formulario = formularioanimal()

    return render(request, 'crear_animales.html', {'formulario': formulario})


def listado_animales(request):
    
    formulario = formulariobusqueda(request.GET)
    if formulario.is_valid():
        animal_buscado = formulario.cleaned_data['especie']
        alimentacion_buscada = formulario.cleaned_data['alimentacion']
        animales = Animal.objects.filter(especie__icontains=animal_buscado, alimentacion__icontains=alimentacion_buscada)
    
    
    return render(request, 'listado_animales.html', {'animales': animales, 'formulario': formulario})

def ver_animales(request, id_animal):
    
    animal = Animal.objects.get(id=id_animal)
    
    return render(request, 'ver_animales.html', {'animal':animal})

def eliminar_animal(request, id_animal):
    
    animal = Animal.objects.get(id=id_animal)
    animal.delete()
    
    return redirect('listado_animales')

def actualizar_animal(request, id_animal):
    
    animal_a_actualizar = Animal.objects.get(id=id_animal)
    
    if request.method == 'POST':
        formulario = formularioactualizar(request.POST)
        if formulario.is_valid():
            especie = formulario.cleaned_data['especie']
            alimentacion = formulario.cleaned_data['alimentacion']
            
            animal_a_actualizar.especie = especie
            animal_a_actualizar.alimentacion = alimentacion
            
            animal_a_actualizar.save()
            
            return redirect('listado_animales')
    else:
        formulario = formularioactualizar(
            initial={
                'especie': animal_a_actualizar.especie ,
                'alimentacion': animal_a_actualizar.alimentacion
                }
            )
    
    return render(request, 'actualizar_animal.html', {'formulario' : formulario, 'animal': animal_a_actualizar})