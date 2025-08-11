# precios/urls.py
from django.urls import path
from . import views

app_name = 'precios'

urlpatterns = [
    path('', views.Alimentos.as_view(), name='lista_precios'),         
    # path('crear/', views.crear_alimento, name='crear_alimento'),
    # path('<int:id>/', views.ver_alimento, name='ver_alimento'),
    # path('<int:id>/eliminar/', views.eliminar_alimento, name='eliminar_alimento'),
    # path('<int:id>/actualizar/', views.actualizar_alimento, name='actualizar_alimento'),
]
