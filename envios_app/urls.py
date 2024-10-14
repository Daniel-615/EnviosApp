from django.urls import path
from .views import (
    listar_vehiculos_view,
    obtener_vehiculo_view,
    crear_vehiculo_view,
    actualizar_vehiculo_view,
    eliminar_vehiculo_view
)
urlpatterns = [
    path('vehiculos/', listar_vehiculos_view, name='listar_vehiculos'),
    path('vehiculos/<int:id>/', obtener_vehiculo_view, name='obtener_vehiculo'),
    path('vehiculos/nuevo/', crear_vehiculo_view, name='crear_vehiculo'),
    path('vehiculos/actualizar/<int:id>/', actualizar_vehiculo_view, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<int:id>/', eliminar_vehiculo_view, name='eliminar_vehiculo'),
]