from .view.AsignacionView import (
    listar_asignaciones,
    obtener_asignacion,
    crear_asignacion,
    actualizar_asignacion,
    eliminar_asignacion
)
from .view.ClienteView import (
    listar_clientes,
    obtener_cliente,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)
from .view.VehiculoView import (
    listar_vehiculos,
    obtener_vehiculo,
    crear_vehiculo,
    actualizar_vehiculo,
    eliminar_vehiculo
)
from .view.EnvioView import(
    listar_envios,
    obtener_envio,
    crear_envio,
    actualizar_envio,
    eliminar_envio
)
from .view.FacturacionDetalleView import(
    listar_facturacion_detalle,
    obtener_facturacion_detalle,
    crear_facturacion_detalle,
    actualizar_facturacion_detalle,
    eliminar_facturacion_detalle
)
from .view.FacturacionView import(
    listar_facturaciones,
    obtener_facturacion,
    crear_facturacion,
    actualizar_facturacion,
    eliminar_facturacion
)
from .view.PaqueteView import(
    listar_paquetes,
    obtener_paquete,
    crear_paquete,
    actualizar_paquete,
    eliminar_paquete
)
from .view.RastreoView import(
    listar_rastreos,
    obtener_rastreo,
    crear_rastreo,
    actualizar_rastreo,
    eliminar_rastreo
)
from .view.TransportistaView import(
    listar_transportistas,
    obtener_transportista,
    crear_transportista,
    actualizar_transportista,
    eliminar_transportista
)
from .view.UbicacionView import(
    listar_ubicaciones,
    obtener_ubicacion,
    crear_ubicacion,
    actualizar_ubicacion,
    eliminar_ubicacion
)

def listar_transportista_view(request):
    return listar_transportistas(request)
def obtener_transportista_view(request,id):
    return obtener_transportista(request,id)
def crear_transportista_view(request):
    return crear_transportista(request)
def actualizar_transportista_view(request,id):
    return actualizar_transportista(request,id)
def eliminar_transportista_view(request,id):
    return eliminar_transportista(request,id)
def listar_paquete_view(request):
    return listar_paquetes(request)
def obtener_paquete_view(request,id):
    return obtener_paquete(request,id)
def crear_paquete_view(request):
    return crear_paquete(request)
def actualizar_paquete_view(request,id):
    return actualizar_paquete(request,id)
def eliminar_paquete_view(request,id):
    return eliminar_paquete(request,id)
def listar_rastreo_view(request):
    return listar_rastreos(request)
def obtener_rastreo_view(request,id):
    return obtener_rastreo(request,id)
def crear_rastreo_view(request):
    return crear_rastreo(request)
def actualizar_rastreo_view(request,id):
    return actualizar_rastreo(request,id)
def eliminar_rastreo_view(request,id):
    return eliminar_rastreo(request,id)
def listar_ubicacion_view(request):
    return listar_ubicaciones(request)
def obtener_ubicacion_view(request,id):
    return obtener_ubicacion(request,id)
def crear_ubicacion_view(request):
    return crear_ubicacion(request)
def actualizar_ubicacion_view(request,id):
    return actualizar_ubicacion(request,id)
def eliminar_ubicacion_view(request,id):
    return eliminar_ubicacion(request,id)
def listar_facturacion_view(request):
    return listar_facturaciones(request)
def obtener_facturacion_view(request,id):
    return obtener_facturacion(request,id)
def crear_facturacion_view(request):
    return crear_facturacion(request)
def actualizar_facturacion_view(request,id):
    return actualizar_facturacion(request,id)
def eliminar_facturacion_view(request,id):
    return eliminar_facturacion(request,id)
def listar_facturacion_detalle_view(request):
    return listar_facturacion_detalle(request)
def obtener_facturacion_detalle_view(request,id):
    return obtener_facturacion_detalle(request,id)
def crear_facturacion_detalle_view(request):
    return crear_facturacion_detalle(request)
def actualizar_facturacion_detalle_view(request,id):
    return actualizar_facturacion_detalle(request,id)
def eliminar_facturacion_detalle_view(request,id):
    return eliminar_facturacion_detalle(request,id)
def listar_envio_view(request):
    return listar_envios(request)
def obtener_envio_view(request,id):
    return obtener_envio(request,id)
def crear_envio_view(request):
    return crear_envio(request)
def actualizar_envio_view(request,id):
    return actualizar_envio(request,id)
def eliminar_envio_view(request,id):
    return eliminar_envio(request,id)
def listar_cliente_view(request):
    return listar_clientes(request)
def obtener_cliente_view(request,id):
    return obtener_cliente(request,id)
def crear_cliente_view(request):
    return crear_cliente(request)
def actualizar_cliente_view(request,id):
    return actualizar_cliente(request,id)
def eliminar_cliente_view(request,id):
    return eliminar_cliente(request,id)
def listar_asignacion_view(request):
    return listar_asignaciones(request)
def obtener_asignacion_view(request,id):
    return obtener_asignacion(request,id)
def crear_asignacion_view(request):
    return crear_asignacion(request)
def actualizar_asignacion_view(request,id):
    return actualizar_asignacion(request,id)
def eliminar_asignacion_view(request,id):
    return eliminar_asignacion(request,id)
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