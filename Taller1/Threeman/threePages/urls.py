from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('creado/', views.creado, name='creado'),
    path('listarClientes/', views.listarClientes, name='listarClientes'),
    path('cliente/<int:cliente_id>/', views.verCliente, name='verCliente'),
    path('cliente/<int:cliente_id>/borrar/', views.borrarCliente, name='borrarCliente'),
]