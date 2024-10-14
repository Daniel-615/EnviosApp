from ..models import AsignacionVehiculoTransportista as Asignacion
from django.core.exceptions import ObjectDoesNotExist

class AsignacionController:
    
    @staticmethod
    def obtener_asignaciones():
        """Obtiene todas las asignaciones."""
        return Asignacion.objects.all()

    @staticmethod
    def obtener_asignacion_id(id_asignacion):
        """Obtiene una asignación por su ID."""
        try:
            return Asignacion.objects.get(id_asignacion=id_asignacion)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_asignacion(transportista, vehiculo, fecha_fin=None):
        """Crea una nueva asignación de transportista a vehículo."""
        nueva_asignacion = Asignacion.objects.create(
            transportista=transportista,
            vehiculo=vehiculo,
            fecha_fin_asignacion=fecha_fin
        )
        return nueva_asignacion

    @staticmethod
    def actualizar_asignacion(id_asignacion, datos):
        """Actualiza los campos de una asignación existente."""
        asignacion = AsignacionController.obtener_asignacion_id(id_asignacion)
        if asignacion:
            for key, value in datos.items():
                if hasattr(asignacion, key):
                    setattr(asignacion, key, value)
            asignacion.save()
            return asignacion
        return None

    @staticmethod
    def eliminar_asignacion(id_asignacion):
        """Elimina una asignación por su ID."""
        asignacion = AsignacionController.obtener_asignacion_id(id_asignacion)
        if asignacion:
            asignacion.delete()
            return True
        return False
