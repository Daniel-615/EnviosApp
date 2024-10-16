from ..models import Cliente
from django.core.exceptions import ObjectDoesNotExist

class ClienteController:

    @staticmethod
    def obtener_clientes():
        """Obtiene todos los clientes."""
        try:
            return Cliente.objects.all()
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def obtener_cliente_id(id_cliente):
        """Obtiene un cliente por su ID."""
        try:
            return Cliente.objects.get(id=id_cliente)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def crear_cliente(nombre, apellido, correo, telefono):
        """Crea un nuevo cliente."""
        try:
            nuevo_cliente = Cliente.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                telefono=telefono
            )
            return nuevo_cliente
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def actualizar_cliente(id_cliente, datos):
        """Actualiza los datos de un cliente existente."""
        try:
            cliente = ClienteController.obtener_cliente_id(id_cliente)
            if cliente:
                for key, value in datos.items():
                    if hasattr(cliente, key):
                        setattr(cliente, key, value)
                cliente.save()
                return cliente
            return None
        except Exception as e:
            print(f"Error: {e}")
    @staticmethod
    def eliminar_cliente(id_cliente):
        """Elimina un cliente por su ID."""
        try:
            cliente = ClienteController.obtener_cliente_id(id_cliente)
            if cliente:
                cliente.delete()
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")