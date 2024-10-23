from django.urls import path
from .views import actualizar_asignacion,crear_asignacion,listar_asignaciones,listar_vehiculos,crear_vehiculo,actualizar_vehiculo

urlpatterns = [
    path('asignaciones/editar/<uuid:id>/', actualizar_asignacion, name='actualizar_asignacion'),
    path('asignaciones/crear/',crear_asignacion,name='crear_asignacion'),
    path('asignaciones/listar/',listar_asignaciones,name='listar_asignaciones'),
    path('vehiculo/editar/<uuid:id>/',actualizar_vehiculo,name='actualizar_vehiculo'),
    path('vehiculo/crear/',crear_vehiculo,name='crear_vehiculo'),
    path('vehiculo/listar',listar_vehiculos,name='listar_vehiculos'),
]
