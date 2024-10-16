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

# Actualizar un transportista existente
def actualizar_transportista(request, id):
    if request.method == 'PUT':
        nombre = request.PUT.get('nombre')
        apellido = request.PUT.get('apellido')
        dpi = request.PUT.get('dpi')
        licencia = request.PUT.get('licencia')
        correo = request.PUT.get('correo')
        telefono = request.PUT.get('telefono')
        transportista_actualizado = TransportistaController.actualizar_transportista(id, nombre, apellido, dpi, licencia, correo, telefono)
        if transportista_actualizado:
            return JsonResponse(transportista_actualizado.to_dict())
        return JsonResponse({'error': 'Transportista no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Eliminar un transportista
def eliminar_transportista(request, id):
    if request.method == 'DELETE':
        transportista_eliminado = TransportistaController.eliminar_transportista(id)
        if transportista_eliminado:
            return JsonResponse({'mensaje': 'Transportista eliminado correctamente'}, status=200)
        return JsonResponse({'error': 'Transportista no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
