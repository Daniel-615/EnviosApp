from ..models import Facturacion_detalle
from django.core.exceptions import ObjectDoesNotExist

class FacturacionDetalleController:
    
    @staticmethod
    def obtener_facturacion_detalles():
        """Obtiene todos los detalles de facturación."""
        return Facturacion_detalle.objects.all()

    @staticmethod
    def obtener_facturacion_detalle_id(id_detalle):
        """Obtiene un detalle de facturación por su ID."""
        try:
            return Facturacion_detalle.objects.get(id=id_detalle)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_facturacion_detalle(facturacion, producto, cantidad, precio_unitario):
        """Crea un nuevo detalle de facturación."""
        return Facturacion_detalle.objects.create(
            facturacion=facturacion,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario
        )

    @staticmethod
    def actualizar_facturacion_detalle(id_detalle, datos):
        """Actualiza un detalle de facturación existente."""
        detalle = FacturacionDetalleController.obtener_facturacion_detalle_id(id_detalle)
        if detalle:
            for key, value in datos.items():
                if hasattr(detalle, key):
                    setattr(detalle, key, value)
            detalle.save()
            return detalle
        return None

    @staticmethod
    def eliminar_facturacion_detalle(id_detalle):
        """Elimina un detalle de facturación por su ID."""
        detalle = FacturacionDetalleController.obtener_facturacion_detalle_id(id_detalle)
        if detalle:
            detalle.delete()
            return True
        return False
