from django.http import JsonResponse
from ..controllers import TransportistaController

# Listar transportistas
def listar_transportistas(request):
    transportistas = TransportistaController.obtener_transportistas()
    data = list(transportistas.values())
    return JsonResponse(data, safe=False)

# Obtener transportista por ID
def obtener_transportista(request, id):
    transportista = TransportistaController.obtener_transportista_id(id)
    if transportista:
        return JsonResponse(transportista.to_dict())
    return JsonResponse({'error': 'Transportista no encontrado'}, status=404)

# Crear un nuevo transportista
def crear_transportista(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        licencia = request.POST.get('licencia')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        transportista = TransportistaController.crear_transportista(nombre, apellido, dpi, licencia, correo, telefono)
        return JsonResponse(transportista.to_dict(), status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
