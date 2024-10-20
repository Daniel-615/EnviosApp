from ..models import Rastreo
class RastreoController:

    @staticmethod
    def obtener_rastreos():
        return Rastreo.objects.all()

    @staticmethod
    def obtener_rastreo_id(id_rastreo):
        return Rastreo.objects.get(id_rastreo=id_rastreo)

    @staticmethod
    def crear_rastreo(id_envio, ubicacion_actual, estado_paquete='en_transito', observaciones=''):
        return Rastreo.objects.create(
            id_envio=id_envio,
            ubicacion_actual=ubicacion_actual,
            estado_paquete=estado_paquete,
            observaciones=observaciones
        )

    @staticmethod
    def actualizar_rastreo(id_rastreo, datos):
        rastreo = RastreoController.obtener_rastreo_id(id_rastreo)
        for key, value in datos.items():
            setattr(rastreo, key, value)
        rastreo.save()
        return rastreo

    @staticmethod
    def eliminar_rastreo(id_rastreo):
        rastreo = RastreoController.obtener_rastreo_id(id_rastreo)
        rastreo.delete()
