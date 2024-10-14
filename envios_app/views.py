from .views.AsignacionView import (
    listar_asignaciones,
    obtener_asignacion,
    crear_asignacion,
    actualizar_asignacion,
    eliminar_asignacion
)
from .views.ClienteView import (
    listar_clientes,
    obtener_cliente,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)
from .views.VehiculoView import (
    listar_vehiculos,
    obtener_vehiculo,
    crear_vehiculo,
    actualizar_vehiculo,
    eliminar_vehiculo
)
def listar_vehiculo_view(request):
    return listar_vehiculos(request)
def obtener_vehiculo_view(request,id):
    return obtener_vehiculo(request,id)
def crear_vehiculo_view(request):
    return crear_vehiculo(request)
def actualizar_vehiculo_view(request,id):
    return actualizar_vehiculo(request,id)
def eliminar_vehiculo_view(request,id):
    return eliminar_vehiculo(request,id)