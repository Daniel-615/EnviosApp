from ..models import Rastreos
class RastreosController():
    @staticmethod
    def obtener_rastreos():
        return Rastreos.objects.all()
    @staticmethod
    def obtener_rastreo_id(id):
        return Rastreos.objects.get(id=id)