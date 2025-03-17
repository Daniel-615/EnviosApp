from ..models import AsignacionVehiculoTransportista as Asignacion
class AsignacionController:
    @staticmethod
    def obtener_asignaciones():
        return Asignacion.objects.all()
    def obtener_asignacion_id(id):
        return Asignacion.objects.get(id=id)
    @staticmethod
    def crear_asignacion(transportista, vehiculo, fecha_fin=None):
        return Asignacion.objects.create(
            transportista=transportista,
            vehiculo=vehiculo,
            fecha_fin_asignacion=fecha_fin
        )

    @staticmethod
    def actualizar_asignacion(id, datos):
        asignacion = AsignacionController.obtener_asignacion_id(id)
        for key, value in datos.items():
            setattr(asignacion, key, value)
        asignacion.save()
        return asignacion

    @staticmethod
    def eliminar_asignacion(id):
        asignacion = AsignacionController.obtener_asignacion_id(id)
        asignacion.delete()