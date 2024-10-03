from ..models import Facturacion
class FacturacionController():
    @staticmethod
    def obtener_facturacion():
        return Facturacion.object.all()
    def obtener_facturacion(id):
        return Facturacion.object.get(id=id)