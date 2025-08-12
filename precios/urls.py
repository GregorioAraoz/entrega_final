# precios/urls.py
from django.urls import path
from precios import views

app_name = 'precios'

urlpatterns = [
    path('', views.Alimentos.as_view(), name='lista_precios'),         
    path('crear/', views.CrearAlimento.as_view(), name='crear_alimento'),
    path('<int:pk>/', views.Ver_alimento.as_view(), name='ver_alimento'),
    path('<int:pk>/eliminar/', views.Eliminar_Alimento.as_view(), name='eliminar_alimento'),
    path('<int:pk>/actualizar/', views.Actualizar_Alimento.as_view(), name='actualizar_alimento'),
]
