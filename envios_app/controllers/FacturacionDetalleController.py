from ..models import Facturacion_detalle
class FacturacionDetalleController:
    @staticmethod
    def obtener_facturacion_detalle():
        return Facturacion_detalle.objects.all()
    @staticmethod
    def obtener_facturacion_id(id):
        return Facturacion_detalle.objects.get(id=id)
    