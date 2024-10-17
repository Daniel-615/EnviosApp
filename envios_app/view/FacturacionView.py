from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers.FacturacionController import FacturacionController

@require_http_methods(["GET"])
def listar_facturaciones(request):
    facturaciones = FacturacionController.obtener_facturaciones()
    data = list(facturaciones.values())
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def obtener_facturacion(request, id):
    facturacion = FacturacionController.obtener_facturacion_id(id)
    if facturacion:
        return JsonResponse(facturacion.to_dict())
    return JsonResponse({'error': 'Facturación no encontrada'}, status=404)


@require_http_methods(["POST"])
def crear_facturacion(request):
    cliente = request.POST.get('cliente')
    total = request.POST.get('total')
    fecha = request.POST.get('fecha')
    
    if cliente and total and fecha:
        facturacion = FacturacionController.crear_facturacion(cliente, total, fecha)
        return JsonResponse(facturacion.to_dict(), status=201)
    
    return JsonResponse({'error': 'Datos incompletos'}, status=400)


@require_http_methods(["PUT"])
def actualizar_facturacion(request, id):
    datos = request.POST.dict()  
    facturacion_actualizada = FacturacionController.actualizar_facturacion(id, datos)
    
    if facturacion_actualizada:
        return JsonResponse(facturacion_actualizada.to_dict())
    return JsonResponse({'error': 'Facturación no encontrada'}, status=404)


@require_http_methods(["DELETE"])
def eliminar_facturacion(request, id):
    eliminado = FacturacionController.eliminar_facturacion(id)
    
    if eliminado:
        return JsonResponse({'mensaje': 'Facturación eliminada correctamente'})
    return JsonResponse({'error': 'Facturación no encontrada'}, status=404)
