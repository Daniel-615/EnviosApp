from ..models import Transportista
class TransportistaController:

    @staticmethod
    def obtener_transportistas():
        return Transportista.objects.all()

    @staticmethod
    def obtener_transportista_id(id_transportista):
        return Transportista.objects.get(id=id_transportista)

    @staticmethod
    def crear_transportista(nombre_transportista, apellido_transportista, dpi_transportista, licencia_transportista, correo_transportista, telefono_transportista):
        return Transportista.objects.create(nombre_transportista=nombre_transportista, apellido_transportista=apellido_transportista,dpi_transportista=dpi_transportista,licencia_transportista=licencia_transportista, correo_transportista=correo_transportista, telefono_transportista=telefono_transportista
        )

    @staticmethod
    def actualizar_transportista(id_transportista, datos):
        transportista = TransportistaController.obtener_transportista_id(id_transportista)
        for key, value in datos.items():
            setattr(transportista, key, value)
        transportista.save()
        return transportista

    @staticmethod
    def eliminar_transportista(id_transportista):
        transportista = TransportistaController.obtener_transportista_id(id_transportista)
        transportista.delete()