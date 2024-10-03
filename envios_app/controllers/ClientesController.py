from ..models import Clientes
class ClientesController():
    @staticmethod
    def obtener_clientes():
        return Clientes.objects.all()
    def obtener_cliente_id(id):
        return Clientes.objects.get(id=id)