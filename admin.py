from django.contrib import admin
from .models import Vehiculo,Transportista,AsignacionVehiculoTransportista,Rastreo,Ubicacion,Cliente,Facturacion,FacturacionDetalle,Paquete,Envio
admin.site.register(Vehiculo)
admin.site.register(Transportista)
admin.site.register(AsignacionVehiculoTransportista)
admin.site.register(Rastreo)
admin.site.register(Ubicacion)
admin.site.register(Cliente)
admin.site.register(Facturacion)
admin.site.register(FacturacionDetalle)
admin.site.register(Paquete)
admin.site.register(Envio)