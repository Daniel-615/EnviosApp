from ..models import Paquete
class PaqueteController:

    @staticmethod
    def obtener_paquetes():
        return Paquete.objects.all()

    @staticmethod 
    def obtener_paquete_id(id_paquete):
        return Paquete.objects.get(id=id_paquete)

    @staticmethod
    def crear_paquete(id_envio, descripcion_paquete, peso, dimensiones, valor_declarado):
        return Paquete.objects.create(
            id_envio=id_envio,
            descripcion_paquete=descripcion_paquete,
            peso=peso,
            dimensiones=dimensiones,
            valor_declarado=valor_declarado
        )

    @staticmethod
    def actualizar_paquete(id_paquete, datos):
        paquete = PaqueteController.obtener_paquete_id(id_paquete)
        for key, value in datos.items():
            setattr(paquete, key, value)
        paquete.save()
        return paquete

    @staticmethod
    def eliminar_paquete(id_paquete):
        paquete = PaqueteController.obtener_paquete_id(id_paquete)
        paquete.delete()
