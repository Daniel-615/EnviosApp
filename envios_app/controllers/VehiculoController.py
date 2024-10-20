from ..models import Vehiculo
from django.core.exceptions import ObjectDoesNotExist

class VehiculoController:

    @staticmethod
    def obtener_vehiculos():
        """Obtiene todos los vehículos."""
        return Vehiculo.objects.all()

    @staticmethod
    def obtener_vehiculo_id(id_vehiculo):
        """Obtiene un vehículo por su ID."""
        try:
            return Vehiculo.objects.get(id=id_vehiculo)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_vehiculo(marca, modelo, placa, capacidad_carga, estado_vehiculo):
        """Crea un nuevo vehículo."""
        return Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            placa=placa,
            capacidad_carga=capacidad_carga,
            estado_vehiculo=estado_vehiculo
        )

    @staticmethod
    def actualizar_vehiculo(id_vehiculo, datos):
        """Actualiza los datos de un vehículo existente."""
        vehiculo = VehiculoController.obtener_vehiculo_id(id_vehiculo)
        if vehiculo:
            for key, value in datos.items():
                if hasattr(vehiculo, key):
                    setattr(vehiculo, key, value)
            vehiculo.save()
            return vehiculo
        return None

    @staticmethod
    def eliminar_vehiculo(id_vehiculo):
        """Elimina un vehículo por su ID."""
        vehiculo = VehiculoController.obtener_vehiculo_id(id_vehiculo)
        if vehiculo:
            vehiculo.delete()
            return True
        return False