from ..models import Vehiculo
class VehiculoController:
    @staticmethod
    def obtener_vehiculos():
        return Vehiculo.objects.all()
    def obtener_vehiculo_id(id):
        return Vehiculo.objects.get(id=id)