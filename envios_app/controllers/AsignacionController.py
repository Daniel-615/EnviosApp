from ..models import AsignacionVehiculoTransportista as Asignacion
class AsignacionController:
    @staticmethod
    def obtener_asignaciones():
        return Asignacion.objects.all()
    def obtener_asignacion_id(id):
        return Asignacion.objects.get(id=id)