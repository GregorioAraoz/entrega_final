
from django.urls import path
from app_inicial.views import saludo, saludo_template, saludo_con_cargador, saludo_con_render, condicion_y_bucle, app_inicial, crear_animales

urlpatterns = [
    path('', app_inicial, name='inicio'),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo),
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_template)
    # path('saludo/<str:nombre>/<str:apellido>/', saludo_con_cargador),
    path('saludo/<str:nombre>/<str:apellido>/', saludo_con_render),
    path('template-prueba/', condicion_y_bucle, name='condicion_y_bucle'),
    path('animal/crear/<str:especie>/<str:alimentacion>/', crear_animales)
]