from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f')<h1>{fecha.strftime('%H:%M:%S')}: Hola {nombre} {apellido}</h1>')

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