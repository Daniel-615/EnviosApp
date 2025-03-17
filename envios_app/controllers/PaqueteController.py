from ..models import Paquete
class PaqueteController:
    @staticmethod
    def obtener_paquetes():
        return Paquete.objects.all()
    @staticmethod 
    def obtener_paquete_id(id):
        return Paquete.objects.get(id=id)
    @staticmethod
    def crear_paquete(envio, descripcion, peso, dimensiones, valor):
        return Paquete.objects.create(
            id_envio=envio,
            descripcion_paquete=descripcion,
            peso=peso,
            dimensiones=dimensiones,
            valor_declarado=valor
        )

    @staticmethod
    def actualizar_paquete(id, datos):
        paquete = PaqueteController.obtener_paquete_id(id)
        for key, value in datos.items():
            setattr(paquete, key, value)
        paquete.save()
        return paquete

    @staticmethod
    def eliminar_paquete(id):
        paquete = PaqueteController.obtener_paquete_id(id)
        paquete.delete()