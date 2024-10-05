from ..models import Ubicacion
class UbicacionController():
    @staticmethod
    def obtener_ubicacion():
        return Ubicacion.objects.all()
    @staticmethod 
    def obtener_ubicacion_id(id):
        return Ubicacion.objects.get()