from ..models import Ubicacion
from django.core.exceptions import ObjectDoesNotExist

class UbicacionController:
    
    @staticmethod
    def obtener_ubicaciones():
        """Obtiene todas las ubicaciones registradas."""
        return Ubicacion.objects.all()

    @staticmethod
    def obtener_ubicacion_id(id_ubicacion):
        """Obtiene una ubicación por su ID."""
        try:
            return Ubicacion.objects.get(id=id_ubicacion)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_ubicacion(nombre, direccion, ciudad, estado):
        """Crea una nueva ubicación."""
        return Ubicacion.objects.create(
            nombre=nombre,
            direccion=direccion,
            ciudad=ciudad,
            estado=estado
        )
    
    @staticmethod
    def actualizar_ubicacion(id_ubicacion, datos):
        """Actualiza una ubicación existente con nuevos datos."""
        ubicacion = UbicacionController.obtener_ubicacion_id(id_ubicacion)
        if ubicacion:
            for key, value in datos.items():
                setattr(ubicacion, key, value)
            ubicacion.save()
            return ubicacion
        return None

    @staticmethod
    def eliminar_ubicacion(id_ubicacion):
        """Elimina una ubicación por su ID."""
        ubicacion = UbicacionController.obtener_ubicacion_id(id_ubicacion)
        if ubicacion:
            ubicacion.delete()
            return True
        return False
