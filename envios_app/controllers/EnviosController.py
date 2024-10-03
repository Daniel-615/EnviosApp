from ..models import Envios
class Envios:
    @staticmethod
    def obtener_envios():
        return Envios.objects.all()
    @staticmethod
    def obtener_envio_id(id):
        return Envios.object.get(id=id)