from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers import UbicacionController

# Listar todas las ubicaciones
@require_http_methods(["GET"])
def listar_ubicaciones(request):
    ubicaciones = UbicacionController.obtener_ubicaciones()
    data = list(ubicaciones.values())
    return JsonResponse(data, safe=False)

# Obtener una ubicación por su ID
@require_http_methods(["GET"])
def obtener_ubicacion(request, id):
    ubicacion = UbicacionController.obtener_ubicacion_id(id)
    if ubicacion:
        return JsonResponse(ubicacion.to_dict())
    return JsonResponse({'error': 'Ubicación no encontrada'}, status=404)

# Crear una nueva ubicación
@require_http_methods(["POST"])
def crear_ubicacion(request):
    nombre = request.POST.get('nombre')
    direccion = request.POST.get('direccion')
    ciudad = request.POST.get('ciudad')
    estado = request.POST.get('estado')
    
    if nombre and direccion and ciudad and estado:
        ubicacion = UbicacionController.crear_ubicacion(nombre, direccion, ciudad, estado)
        return JsonResponse(ubicacion.to_dict(), status=201)
    
    return JsonResponse({'error': 'Datos incompletos'}, status=400)

# Actualizar una ubicación existente por su ID
@require_http_methods(["PUT"])
def actualizar_ubicacion(request, id):
    datos = request.POST.dict()  # Convertir los datos enviados a un diccionario
    ubicacion_actualizada = UbicacionController.actualizar_ubicacion(id, datos)
    
    if ubicacion_actualizada:
        return JsonResponse(ubicacion_actualizada.to_dict())
    return JsonResponse({'error': 'Ubicación no encontrada'}, status=404)

# Eliminar una ubicación por su ID
@require_http_methods(["DELETE"])
def eliminar_ubicacion(request, id):
    eliminado = UbicacionController.eliminar_ubicacion(id)
    
    if eliminado:
        return JsonResponse({'mensaje': 'Ubicación eliminada correctamente'})
    return JsonResponse({'error': 'Ubicación no encontrada'}, status=404)
