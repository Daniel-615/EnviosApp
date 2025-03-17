from ..models import Rastreo
class RastreoController:
    @staticmethod
    def obtener_Rastreo():
        return Rastreo.objects.all()
    @staticmethod
    def obtener_rastreo_id(id):
        return Rastreo.objects.get(id=id)
    @staticmethod
    def crear_rastreo(envio, ubicacion_actual, estado='en_transito', observaciones=''):
        return Rastreo.objects.create(
            id_envio=envio,
            ubicacion_actual=ubicacion_actual,
            estado_paquete=estado,
            observaciones=observaciones
        )

    @staticmethod
    def actualizar_rastreo(id, datos):
        rastreo = RastreoController.obtener_rastreo_id(id)
        for key, value in datos.items():
            setattr(rastreo, key, value)
        rastreo.save()
        return rastreo

    @staticmethod
    def eliminar_rastreo(id):
        rastreo = RastreoController.obtener_rastreo_id(id)
        rastreo.delete()