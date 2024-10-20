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
    listar_cliente_view,
    obtener_cliente_view,
    crear_cliente_view,
    actualizar_cliente_view,
    eliminar_cliente_view,
    listar_transportista_view,
    obtener_transportista_view,
    crear_transportista_view,
    actualizar_transportista_view,
    eliminar_transportista_view,
    listar_paquete_view,
    obtener_paquete_view,
    crear_paquete_view,
    actualizar_paquete_view,
    eliminar_paquete_view,
    listar_rastreo_view,
    obtener_rastreo_view,
    crear_rastreo_view,
    actualizar_rastreo_view,
    eliminar_rastreo_view,
    listar_ubicacion_view,
    obtener_ubicacion_view,
    crear_ubicacion_view,
    actualizar_ubicacion_view,
    eliminar_ubicacion_view,
    listar_facturacion_view,
    obtener_facturacion_view,
    crear_facturacion_view,
    actualizar_facturacion_view,
    eliminar_facturacion_view,
    listar_facturacion_detalle_view,
    obtener_facturacion_detalle_view,
    crear_facturacion_detalle_view,
    actualizar_facturacion_detalle_view,
    eliminar_facturacion_detalle_view,
    listar_envio_view,
    obtener_envio_view,
    crear_envio_view,
    actualizar_envio_view,
    eliminar_envio_view
)

urlpatterns = [
    path('vehiculos/', listar_vehiculo_view, name='listar_vehiculos'),
    path('vehiculos/<uuid:id>/', obtener_vehiculo_view, name='obtener_vehiculo'),
    path('vehiculos/nuevo/', crear_vehiculo_view, name='crear_vehiculo'),
    path('vehiculos/actualizar/<uuid:id>/', actualizar_vehiculo_view, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<uuid:id>/', eliminar_vehiculo_view, name='eliminar_vehiculo'),
    path('asignaciones/', listar_asignacion_view, name='listar_asignaciones'),
    path('asignaciones/<uuid:id>/', obtener_asignacion_view, name='obtener_asignacion'),
    path('asignaciones/crear', crear_asignacion_view, name='crear_asignacion'),
    path('asignaciones/actualizar/<uuid:id>/', actualizar_asignacion_view, name='actualizar_asignacion'),
    path('asignaciones/eliminar/<uuid:id>/', eliminar_asignacion_view, name='eliminar_asignacion'),
    path('clientes/', listar_cliente_view, name='listar_clientes'),
    path('clientes/<uuid:id>/', obtener_cliente_view, name='obtener_cliente'),
    path('clientes/crear/', crear_cliente_view, name='crear_cliente'),
    path('clientes/actualizar', actualizar_cliente_view, name='actualizar_cliente'),
    path('clientes/eliminar', eliminar_cliente_view, name='eliminar_cliente'),
    path('transportistas/', listar_transportista_view, name='listar_transportistas'),
    path('transportistas/<uuid:id>/', obtener_transportista_view, name='obtener_transportista'),
    path('transportistas/crear/', crear_transportista_view, name='crear_transportista'),
    path('transportistas/actualizar/<uuid:id>/', actualizar_transportista_view, name='actualizar_transportista'),
    path('transportistas/eliminar/<uuid:id>/', eliminar_transportista_view, name='eliminar_transportista'),
    path('paquetes/', listar_paquete_view, name='listar_paquetes'),
    path('paquetes/<uuid:id>/', obtener_paquete_view, name='obtener_paquete'),
    path('paquetes/crear/', crear_paquete_view, name='crear_paquete'),
    path('paquetes/actualizar/<uuid:id>/', actualizar_paquete_view, name='actualizar_paquete'),
    path('paquetes/eliminar/<uuid:id>/', eliminar_paquete_view, name='eliminar_paquete'),
    path('rastreos/', listar_rastreo_view, name='listar_rastreos'),
    path('rastreos/<uuid:id>/', obtener_rastreo_view, name='obtener_rastreo'),
    path('rastreos/crear/', crear_rastreo_view, name='crear_rastreo'),
    path('rastreos/actualizar/<uuid:id>/', actualizar_rastreo_view, name='actualizar_rastreo'),
    path('rastreos/eliminar/<uuid:id>/', eliminar_rastreo_view, name='eliminar_rastreo'),
    path('ubicaciones/', listar_ubicacion_view, name='listar_ubicaciones'),
    path('ubicaciones/<uuid:id>/', obtener_ubicacion_view, name='obtener_ubicacion'),
    path('ubicaciones/crear/', crear_ubicacion_view, name='crear_ubicacion'),
    path('ubicaciones/actualizar/<uuid:id>/', actualizar_ubicacion_view, name='actualizar_ubicacion'),
    path('ubicaciones/eliminar/<uuid:id>/', eliminar_ubicacion_view, name='eliminar_ubicacion'),
    path('facturaciones/', listar_facturacion_view, name='listar_facturaciones'),
    path('facturaciones/<uuid:id>/', obtener_facturacion_view, name='obtener_facturacion'),
    path('facturaciones/crear/', crear_facturacion_view, name='crear_facturacion'),
    path('facturaciones/actualizar/<uuid:id>/', actualizar_facturacion_view, name='actualizar_facturacion'),
    path('facturaciones/eliminar/<uuid:id>/', eliminar_facturacion_view, name='eliminar_facturacion'),
    path('facturaciones/detalle/', listar_facturacion_detalle_view, name='listar_facturacion_detalle'),
    path('facturaciones/detalle/<uuid:id>/', obtener_facturacion_detalle_view, name='obtener_facturacion_detalle'),
    path('facturaciones/detalle/crear/', crear_facturacion_detalle_view, name='crear_facturacion_detalle'),
    path('facturaciones/detalle/actualizar/<uuid:id>/', actualizar_facturacion_detalle_view, name='actualizar_facturacion_detalle'),
    path('facturaciones/detalle/eliminar/<uuid:id>/', eliminar_facturacion_detalle_view, name='eliminar_facturacion_detalle'),
    path('envios/', listar_envio_view, name='listar_envios'),
    path('envios/<uuid:id>/', obtener_envio_view, name='obtener_envio'),
    path('envios/crear/', crear_envio_view, name='crear_envio'),
    path('envios/actualizar/<uuid:id>/', actualizar_envio_view, name='actualizar_envio'),
    path('envios/eliminar/<uuid:id>/', eliminar_envio_view, name='eliminar_envio'),
]