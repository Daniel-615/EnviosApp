from django.urls import path
from .views import (
    actualizar_asignacion,crear_asignacion,listar_asignaciones,
    listar_vehiculos,crear_vehiculo,actualizar_vehiculo,
    listar_transportistas,crear_transportista,actualizar_transportista,home
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
]
