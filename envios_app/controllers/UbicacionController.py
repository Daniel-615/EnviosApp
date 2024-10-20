from ..models import Ubicacion
class UbicacionController:

    @staticmethod
    def obtener_ubicaciones():
        return Ubicacion.objects.all()

    @staticmethod
    def obtener_ubicacion_id(id_ubicacion):
        return Ubicacion.objects.get(id=id_ubicacion)

    @staticmethod
    def crear_ubicacion(pais, departamento, municipio, direccion):
        return Ubicacion.objects.create(
            pais=pais,
            departamento=departamento,
            municipio=municipio,
            direccion=direccion
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
