from ..models import Transportista
class TransportistaController:
    @staticmethod
    def obtener_transportistas():
        return Transportista.objects.all()
    @staticmethod
    def obtener_transportista_id(id):
        return Transportista.objects.get(id=id)
    @staticmethod
    def crear_transportista(nombre, apellido, dpi, licencia, correo, telefono):
        return Transportista.objects.create(
            nombre_transportista=nombre,
            apellido_transportista=apellido,
            dpi_transportista=dpi,
            licencia_transportista=licencia,
            correo_transportista=correo,
            telefono_transportista=telefono
        )

    @staticmethod
    def actualizar_transportista(id, datos):
        transportista = TransportistaController.obtener_transportista_id(id)
        for key, value in datos.items():
            setattr(transportista, key, value)
        transportista.save()
        return transportista

    @staticmethod
    def eliminar_transportista(id):
        transportista = TransportistaController.obtener_transportista_id(id)
        transportista.delete()