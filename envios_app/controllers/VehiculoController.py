from ..models import Vehiculo
class VehiculoController:
    @staticmethod
    def obtener_vehiculos():
        return Vehiculo.objects.all()
    def obtener_vehiculo_id(id):
        return Vehiculo.objects.get(id=id)
    def crear_vehiculo(matricula, marca, modelo):
        return Vehiculo.objects.create(
            matricula_vehiculo=matricula,
            marca_vehiculo=marca,
            modelo_vehiculo=modelo
        )

    @staticmethod
    def actualizar_vehiculo(id, datos):
        vehiculo = VehiculoController.obtener_vehiculo_id(id)
        for key, value in datos.items():
            setattr(vehiculo, key, value)
        vehiculo.save()
        return vehiculo

    @staticmethod
    def eliminar_vehiculo(id):
        vehiculo = VehiculoController.obtener_vehiculo_id(id)
        vehiculo.delete()