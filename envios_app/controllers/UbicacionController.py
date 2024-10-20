from ..models import Ubicacion
class UbicacionController:

    @staticmethod
    def obtener_ubicaciones():
        return Ubicacion.objects.all()

    @staticmethod
    def obtener_ubicacion_id(id_ubicacion):
        return Ubicacion.objects.get(id_ubicacion=id_ubicacion)

    @staticmethod
    def crear_ubicacion(id_cliente,ciudad,calle,codigo_postal,coordenadas_geograficas,referencias):
        return Ubicacion.objects.create(
            id_cliente=id_cliente,
            ciudad=ciudad,
            calle=calle,
            codigo_postal=codigo_postal,
            coordenadas_geograficas=coordenadas_geograficas,
            referencias=referencias
        )

    @staticmethod
    def actualizar_ubicacion(id_ubicacion, datos):
        ubicacion = UbicacionController.obtener_ubicacion_id(id_ubicacion)
        for key, value in datos.items():
            setattr(ubicacion, key, value)
        ubicacion.save()
        return ubicacion

    @staticmethod
    def eliminar_ubicacion(id_ubicacion):
        ubicacion = UbicacionController.obtener_ubicacion_id(id_ubicacion)
        ubicacion.delete()
