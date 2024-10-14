from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers import AsignacionController

# Listar todas las asignaciones
@require_http_methods(["GET"])
def listar_asignaciones(request):
    try:
        asignaciones = AsignacionController.obtener_asignaciones()
        data = list(asignaciones.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Obtener una asignación por su ID
@require_http_methods(["GET"])
def obtener_asignacion(request, id):
    asignacion = AsignacionController.obtener_asignacion_id(id)
    if asignacion:
        return JsonResponse(asignacion.to_dict())
    return JsonResponse({'error': 'Asignación no encontrada'}, status=404)

# Crear una nueva asignación
@require_http_methods(["POST"])
def crear_asignacion(request):
    transportista = request.POST.get('transportista')
    vehiculo = request.POST.get('vehiculo')
    fecha_fin = request.POST.get('fecha_fin', None)

    if transportista and vehiculo:
        try:
            nueva_asignacion = AsignacionController.crear_asignacion(
                transportista, vehiculo, fecha_fin
            )
            return JsonResponse(nueva_asignacion.to_dict(), status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Datos incompletos'}, status=400)

# Actualizar una asignación existente
@require_http_methods(["PUT"])
def actualizar_asignacion(request, id):
    datos = request.POST.dict()  # Convertir los datos enviados a un diccionario
    try:
        asignacion_actualizada = AsignacionController.actualizar_asignacion(id, datos)
        if asignacion_actualizada:
            return JsonResponse(asignacion_actualizada.to_dict())
        return JsonResponse({'error': 'Asignación no encontrada'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Eliminar una asignación por su ID
@require_http_methods(["DELETE"])
def eliminar_asignacion(request, id):
    try:
        eliminado = AsignacionController.eliminar_asignacion(id)
        if eliminado:
            return JsonResponse({'mensaje': 'Asignación eliminada correctamente'})
        return JsonResponse({'error': 'Asignación no encontrada'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
