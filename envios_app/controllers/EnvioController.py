from ..models import Envio
class EnvioController:
    @staticmethod
    def obtener_envios():
        return Envio.objects.all()
    @staticmethod
    def obtener_envio_id(id):
        return Envio.objects.get(id=id)