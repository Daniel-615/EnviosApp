from ..models import Vehiculo
class VehiculoController:
    @staticmethod
    def obtener_vehiculos():
        """Obtiene todos los vehiculos"""
        try:
            return Vehiculo.objects.all()
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def obtener_vehiculo_id(id):
        """Obtiene un vehiculo por id"""
        try:
            return Vehiculo.objects.get(id=id)
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def crear_vehiculo(matricula, marca, modelo):
        """Crea un nuevo vehiculo"""
        try:
            return Vehiculo.objects.create(
                matricula_vehiculo=matricula,
                marca_vehiculo=marca,
                modelo_vehiculo=modelo
            )
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def actualizar_vehiculo(id, datos):
        """Actualiza su vehiculo por su ID."""
        try:
            vehiculo = VehiculoController.obtener_vehiculo_id(id)
            for key, value in datos.items():
                setattr(vehiculo, key, value)
            vehiculo.save()
            return vehiculo
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def eliminar_vehiculo(id):
        """Elimina un vehiculo por su ID."""
        try:
            vehiculo = VehiculoController.obtener_vehiculo_id(id)
            if vehiculo:
                vehiculo.delete()
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")