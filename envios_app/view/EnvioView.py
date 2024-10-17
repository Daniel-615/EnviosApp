from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers.EnvioController import EnvioController


@require_http_methods(["GET"])
def listar_envios(request):
    envios = EnvioController.obtener_envios()
    data = list(envios.values())
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def obtener_envio(request, id):
    envio = EnvioController.obtener_envio_id(id)
    if envio:
        return JsonResponse(envio.to_dict())
    return JsonResponse({'error': 'Envío no encontrado'}, status=404)


@require_http_methods(["POST"])
def crear_envio(request):
    asignacion = request.POST.get('asignacion')
    ubicacion = request.POST.get('ubicacion')
    estado = request.POST.get('estado', 'pendiente')
    
    if asignacion and ubicacion:
        envio = EnvioController.crear_envio(asignacion, ubicacion, estado)
        return JsonResponse(envio.to_dict(), status=201)
    
    return JsonResponse({'error': 'Datos incompletos'}, status=400)


@require_http_methods(["PUT"])
def actualizar_envio(request, id):
    datos = request.POST.dict() 
    envio_actualizado = EnvioController.actualizar_envio(id, datos)
    
    if envio_actualizado:
        return JsonResponse(envio_actualizado.to_dict())
    return JsonResponse({'error': 'Envío no encontrado'}, status=404)


@require_http_methods(["DELETE"])
def eliminar_envio(request, id):
    eliminado = EnvioController.eliminar_envio(id)
    
    if eliminado:
        return JsonResponse({'mensaje': 'Envío eliminado correctamente'})
    return JsonResponse({'error': 'Envío no encontrado'}, status=404)
