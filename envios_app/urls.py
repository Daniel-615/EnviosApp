from django.urls import path
from .views import (
    listar_vehiculo_view,
    obtener_vehiculo_view,
    crear_vehiculo_view,
    actualizar_vehiculo_view,
    eliminar_vehiculo_view,
    listar_asignacion_view,
    obtener_asignacion_view,
    crear_asignacion_view,
    actualizar_asignacion_view,
    eliminar_asignacion_view,

)
urlpatterns = [
    path('vehiculos/', listar_vehiculo_view, name='listar_vehiculos'),
    path('vehiculos/<uuid:id>/', obtener_vehiculo_view, name='obtener_vehiculo'),
    path('vehiculos/nuevo/', crear_vehiculo_view, name='crear_vehiculo'),
    path('vehiculos/actualizar/<uuid:id>/', actualizar_vehiculo_view, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<uuid:id>/', eliminar_vehiculo_view, name='eliminar_vehiculo'),
    path('asignaciones/',listar_asignacion_view,name='listar_asignaciones'),
    path('asignaciones/<uuid:id>/',obtener_asignacion_view,name='obtener_asignacion'),
    path('asignaciones/crear',crear_asignacion_view,name='crear_asignacion'),
    path('asignaciones/actualizar/<uuid:id>/',actualizar_asignacion_view,name='actualizar_asignacion'),
    path('asignaciones/eliminar/<uuid:id>/',eliminar_asignacion_view,name='eliminar_asignacion')
]