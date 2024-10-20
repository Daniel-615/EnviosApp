from ..models import Facturacion
from django.core.exceptions import ObjectDoesNotExist

class FacturacionController:

    @staticmethod
    def obtener_facturaciones():
        """Obtiene todas las facturaciones."""
        return Facturacion.objects.all()

    @staticmethod
    def obtener_facturacion_id(id_factura):
        """Obtiene una facturación por su ID."""
        try:
            return Facturacion.objects.get(id=id_factura)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_facturacion(id_cliente):
        """Crea una nueva facturación."""
        return Facturacion.objects.create(
            id_cliente=id_cliente
        )

    @staticmethod
    def actualizar_facturacion(id_factura, datos):
        """Actualiza los datos de una facturación existente."""
        facturacion = FacturacionController.obtener_facturacion_id(id_factura)
        if facturacion:
            for key, value in datos.items():
                if hasattr(facturacion, key):
                    setattr(facturacion, key, value)
            facturacion.save()
            return facturacion
        return None

    @staticmethod
    def eliminar_facturacion(id_factura):
        """Elimina una facturación por su ID."""
        facturacion = FacturacionController.obtener_facturacion_id(id_factura)
        if facturacion:
            facturacion.delete()
            return True
        return False
