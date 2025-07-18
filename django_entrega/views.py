from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader

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
        "listado_de_animales": [1, 2, 3, 4, 5, 6]
    })