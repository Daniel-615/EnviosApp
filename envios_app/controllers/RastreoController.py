from ..models import Rastreo
class RastreoController:
    @staticmethod
    def obtener_Rastreo():
        return Rastreo.objects.all()
    @staticmethod
    def obtener_rastreo_id(id):
        return Rastreo.objects.get(id=id)