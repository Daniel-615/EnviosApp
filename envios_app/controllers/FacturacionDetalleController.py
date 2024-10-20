from ..models import FacturacionDetalle
from django.core.exceptions import ObjectDoesNotExist

class FacturacionDetalleController:

    @staticmethod
    def obtener_facturacion_detalles():
        """Obtiene todos los detalles de facturación."""
        return FacturacionDetalle.objects.all()

    @staticmethod
    def obtener_facturacion_detalle_id(id_factura_detalle):
        """Obtiene un detalle de facturación por su ID."""
        try:
            return FacturacionDetalle.objects.get(id=id_factura_detalle)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_facturacion_detalle(id_factura, monto_total, fecha_facturacion, metodo_pago):
        """Crea un nuevo detalle de facturación."""
        return FacturacionDetalle.objects.create(
            id_factura=id_factura,
            monto_total=monto_total,
            fecha_facturacion=fecha_facturacion,
            metodo_pago=metodo_pago
        )

    @staticmethod
    def actualizar_facturacion_detalle(id_factura_detalle, datos):
        """Actualiza un detalle de facturación existente."""
        detalle = FacturacionDetalleController.obtener_facturacion_detalle_id(id_factura_detalle)
        if detalle:
            for key, value in datos.items():
                if hasattr(detalle, key):
                    setattr(detalle, key, value)
            detalle.save()
            return detalle
        return None

    @staticmethod
    def eliminar_facturacion_detalle(id_factura_detalle):
        """Elimina un detalle de facturación por su ID."""
        detalle = FacturacionDetalleController.obtener_facturacion_detalle_id(id_factura_detalle)
        if detalle:
            detalle.delete()
            return True
        return False
