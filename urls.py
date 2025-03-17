from django.urls import path
from .views import (
    actualizar_asignacion,crear_asignacion,listar_asignaciones,
    listar_vehiculos,crear_vehiculo,actualizar_vehiculo,
    listar_transportistas,crear_transportista,actualizar_transportista,home,
    listar_envios,crear_envio,actualizar_envio,
    listar_paquete,crear_paquete,actualizar_paquete
    #mis urls
    )

urlpatterns = [
    path('',home,name='home'),
    path('asignaciones/editar/<uuid:id>/', actualizar_asignacion, name='actualizar_asignacion'),
    path('asignaciones/crear/',crear_asignacion,name='crear_asignacion'),
    path('asignaciones/listar/',listar_asignaciones,name='listar_asignaciones'),
    path('vehiculos/listar',listar_vehiculos,name='listar_vehiculos'),
    path('vehiculos/crear/',crear_vehiculo,name='crear_vehiculo'),
    path('vehiculos/editar/<uuid:id>/',actualizar_vehiculo,name='actualizar_vehiculo'),
    path('transportistas/listar',listar_transportistas,name='listar_transportistas'),
    path('transportistas/crear/',crear_transportista,name='crear_transportista'),
    path('transportistas/editar/<uuid:id>/',actualizar_transportista,name='actualizar_transportista'),
    path('envios/listar/',listar_envios,name='listar_envios'),
    path('envios/crear/',crear_envio,name='crear_envio'),
    path('envios/editar/<uuid:id>/',actualizar_envio,name='actualizar_envio'),
    path('paquete/editar<uuid:id>/',actualizar_paquete, name='actualizar_paquete'),
    path('paquete/crear/',crear_paquete,name='crear_paquete'),
    path('paquete/listar/',listar_paquete,name='listar_paquete')
    #mis path
    ]