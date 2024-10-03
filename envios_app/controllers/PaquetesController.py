from ..models import Paquetes
class Paquetes():
    @staticmethod
    def obtener_paquetes():
        return Paquetes.objects.all()
    @staticmethod 
    def obtener_paquete_id(id):
        return Paquetes.objects.get(id=id)