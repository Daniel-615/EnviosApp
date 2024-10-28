from django.urls import path
from .views import (
    actualizar_asignacion,crear_asignacion,listar_asignaciones,
    listar_vehiculos,crear_vehiculo,actualizar_vehiculo,
    listar_transportistas,crear_transportista,actualizar_transportista,home,
    eliminar_transportista,eliminar_vehiculo,listar_rastreo,crear_rastreo,actualizar_rastreo,
    listar_paquetes, crear_paquete,actualizar_paquete,listar_envios,
    actualizar_envio,crear_envio,listar_ubicaciones,
    crear_ubicacion, actualizar_ubicacion,listar_facturas,crear_factura,
    listar_factura_detalle,crear_factura_detalle,
    listar_clientes,crear_cliente,actualizar_cliente
)

urlpatterns = [
    path('',home,name='home'),

    path('asignaciones/crear/',crear_asignacion,name='crear_asignacion'),
    path('asignaciones/listar/',listar_asignaciones,name='listar_asignaciones'),
    path('asignaciones/editar/<uuid:id_asignacion>/', actualizar_asignacion, name='actualizar_asignacion'),

    path('vehiculos/listar',listar_vehiculos,name='listar_vehiculos'),
    path('vehiculos/crear/',crear_vehiculo,name='crear_vehiculo'),
    path('vehiculos/editar/<uuid:id_vehiculo>/',actualizar_vehiculo,name='actualizar_vehiculo'),
    path('vehiculos/activo/<uuid:id_vehiculo>/',eliminar_vehiculo,name='eliminar_vehiculo'),

    path('transportistas/listar/',listar_transportistas,name='listar_transportistas'),
    path('transportistas/crear/',crear_transportista,name='crear_transportista'),
    path('transportista/editar/<uuid:id_transportista>/',actualizar_transportista, name='actualizar_transportista'),
    path('transportista/activo/<uuid:id_transportista>',eliminar_transportista,name='eliminar_transportista'),

    path('rastreos/listar/',listar_rastreo,name='listar_rastreos'),
    path('rastreos/crear/',crear_rastreo,name='crear_rastreo'),
    path('rastreos/editar/<uuid:id_rastreo>/',actualizar_rastreo,name='actualizar_rastreo'),

    path('paquetes/listar/',listar_paquetes,name='listar_paquetes'),
    path('paquetes/crear/',crear_paquete,name='crear_paquete'),
    path('paquetes/editar/<uuid:id_paquete>/',actualizar_paquete,name='actualizar_paquete'),

    path('envios/listar/',listar_envios,name='listar_envios'),
    path('envios/crear/',crear_envio,name='crear_envio'),
    path('envios/editar/<uuid:id_envio>/',actualizar_envio,name='actualizar_envio'),

    path('ubicacion/listar',listar_ubicaciones,name='listar_ubicaciones'),
    path('ubicacion/crear/',crear_ubicacion,name='crear_ubicacion'),
    path('ubicacion/editar/<uuid:id_ubicacion>/',actualizar_ubicacion,name='actualizar_ubicacion'),

    path('facturas/listar/',listar_facturas,name='listar_facturas'),
    path('facturas/crear/',crear_factura,name='crear_factura'),

    path('facturas/listar/detalle/',listar_factura_detalle,name='listar_facturas_detalle'),
    path('facturas/crear/detalle/',crear_factura_detalle,name='crear_factura_detalle'),
  

    path('clientes/listar/',listar_clientes,name='listar_clientes'),
    path('clientes/crear/',crear_cliente,name='crear_cliente'),
    path('clientes/editar/<uuid:id_cliente>/',actualizar_cliente,name='actualizar_cliente'),
]
