from ..models import Cliente
class ClientesController:
    @staticmethod
    def obtener_clientes():
        return Cliente.objects.all()
    def obtener_cliente_id(id):
        return Cliente.objects.get(id=id)