from django.http import JsonResponse
from ..controllers import FacturacionDetalleController

# Listar todos los detalles de facturación
def listar_facturacion_detalle(request):
    detalles = FacturacionDetalleController.obtener_facturacion_detalles()
    data = list(detalles.values())
    return JsonResponse(data, safe=False)

# Obtener un detalle de facturación por su ID
def obtener_facturacion_detalle(request, id):
    detalle = FacturacionDetalleController.obtener_facturacion_detalle_id(id)
    if detalle:
        return JsonResponse(detalle.to_dict())
    return JsonResponse({'error': 'Detalle de facturación no encontrado'}, status=404)

# Crear un nuevo detalle de facturación
def crear_facturacion_detalle(request):
    if request.method == 'POST':
        facturacion = request.POST.get('facturacion')
        producto = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('precio_unitario')
        detalle = FacturacionDetalleController.crear_facturacion_detalle(facturacion, producto, cantidad, precio_unitario)
        return JsonResponse(detalle.to_dict(), status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Actualizar un detalle de facturación por su ID
def actualizar_facturacion_detalle(request, id):
    if request.method == 'PUT':
        datos = request.POST.dict()  # Convertir los datos enviados a un diccionario
        detalle_actualizado = FacturacionDetalleController.actualizar_facturacion_detalle(id, datos)
        if detalle_actualizado:
            return JsonResponse(detalle_actualizado.to_dict())
        return JsonResponse({'error': 'Detalle de facturación no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Eliminar un detalle de facturación por su ID
def eliminar_facturacion_detalle(request, id):
    if request.method == 'DELETE':
        eliminado = FacturacionDetalleController.eliminar_facturacion_detalle(id)
        if eliminado:
            return JsonResponse({'mensaje': 'Detalle de facturación eliminado correctamente'})
        return JsonResponse({'error': 'Detalle de facturación no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
