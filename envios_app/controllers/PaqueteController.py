from ..models import Paquete
class PaqueteController:
    @staticmethod
    def obtener_paquetes():
        return Paquete.objects.all()
    @staticmethod 
    def obtener_paquete_id(id):
        return Paquete.objects.get(id=id)