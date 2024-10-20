from ..models import Envio
from django.core.exceptions import ObjectDoesNotExist

class EnvioController:

    @staticmethod
    def obtener_envios():
        """Obtiene todos los envíos."""
        return Envio.objects.all()

    @staticmethod
    def obtener_envio_id(id_envio):
        """Obtiene un envío por su ID."""
        try:
            return Envio.objects.get(id=id_envio)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_envio(id_asignacion_transportista, id_ubicacion, fecha_creacion, estado_envio='pendiente'):
        """Crea un nuevo envío."""
        return Envio.objects.create(
            id_asignacion_transportista=id_asignacion_transportista,
            id_ubicacion=id_ubicacion,
            fecha_creacion=fecha_creacion,
            estado_envio=estado_envio
        )

    @staticmethod
    def actualizar_envio(id_envio, datos):
        """Actualiza los datos de un envío existente."""
        envio = EnvioController.obtener_envio_id(id_envio)
        if envio:
            for key, value in datos.items():
                if hasattr(envio, key):
                    setattr(envio, key, value)
            envio.save()
            return envio
        return None

    @staticmethod
    def eliminar_envio(id_envio):
        """Elimina un envío por su ID."""
        envio = EnvioController.obtener_envio_id(id_envio)
        if envio:
            envio.delete()
            return True
        return False
