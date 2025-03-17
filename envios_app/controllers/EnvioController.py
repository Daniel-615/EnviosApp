from ..models import Envio
class EnvioController:
    @staticmethod
    def obtener_envios():
        return Envio.objects.all()
    @staticmethod
    def obtener_envio_id(id):
        return Envio.objects.get(id=id)
    @staticmethod
    def crear_envio(asignacion, ubicacion, estado='pendiente'):
        return Envio.objects.create(
            id_asignacion=asignacion,
            id_ubicacion=ubicacion,
            estado_envio=estado
        )

    @staticmethod
    def actualizar_envio(id, datos):
        envio = EnvioController.obtener_envio_id(id)
        for key, value in datos.items():
            setattr(envio, key, value)
        envio.save()
        return envio

    @staticmethod
    def eliminar_envio(id):
        envio = EnvioController.obtener_envio_id(id)
        envio.delete()