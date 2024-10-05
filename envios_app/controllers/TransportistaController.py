from ..models import Transportista
class TransportistaController:
    @staticmethod
    def obtener_transportistas():
        return Transportista.objects.all()
    @staticmethod
    def obtener_transportista_id(id):
        return Transportista.objects.get(id=id)