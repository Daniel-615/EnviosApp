from ..models import Facturacion
class FacturacionController:
    @staticmethod
    def obtener_facturacion():
        return Facturacion.objects.all()
    def obtener_facturacion(id):
        return Facturacion.objects.get(id=id)