from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers.VehiculoController import VehiculoController


def listar_vehiculos(request):
    vehiculos = VehiculoController.obtener_vehiculos()
    data = list(vehiculos.values())
    return JsonResponse(data, safe=False)


def obtener_vehiculo(request, id):
    vehiculo = VehiculoController.obtener_vehiculo_id(id)
    if vehiculo:
        return JsonResponse(vehiculo.to_dict())
    return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)


@require_http_methods(["POST"])
def crear_vehiculo(request):
    matricula = request.POST.get('matricula')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    if matricula and marca and modelo:
        vehiculo = VehiculoController.crear_vehiculo(matricula, marca, modelo)
        return JsonResponse(vehiculo.to_dict(), status=201)
    return JsonResponse({'error': 'Datos incompletos'}, status=400)

@require_http_methods(["PUT"])
def actualizar_vehiculo(request, id):
    datos = request.POST.dict()  
    try:
        vehiculo_actualizado = VehiculoController.actualizar_vehiculo(id, datos)
        if vehiculo_actualizado:
            return JsonResponse(vehiculo_actualizado.to_dict())
        return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["DELETE"])
def eliminar_vehiculo(request, id):
    try:
        eliminado = VehiculoController.eliminar_vehiculo(id)
        if eliminado:
            return JsonResponse({'mensaje': 'Vehículo eliminado correctamente'})
        return JsonResponse({'error': 'Vehículo no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
