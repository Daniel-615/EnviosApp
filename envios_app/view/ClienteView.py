from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..controllers.ClienteController import ClienteController

# Listar todos los clientes
@require_http_methods(["GET"])
def listar_clientes(request):
    try:
        clientes = ClienteController.obtener_clientes()
        data = list(clientes.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Obtener un cliente por su ID
@require_http_methods(["GET"])
def obtener_cliente(request, id):
    cliente = ClienteController.obtener_cliente_id(id)
    if cliente:
        return JsonResponse(cliente.to_dict())
    return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

# Crear un nuevo cliente
@require_http_methods(["POST"])
def crear_cliente(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    correo = request.POST.get('correo')
    telefono = request.POST.get('telefono')
    
    if nombre and apellido and correo and telefono:
        try:
            cliente = ClienteController.crear_cliente(nombre, apellido, correo, telefono)
            return JsonResponse(cliente.to_dict(), status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Datos incompletos'}, status=400)

# Actualizar un cliente existente por su ID
@require_http_methods(["PUT"])
def actualizar_cliente(request, id):
    datos = request.POST.dict()  # Convertir los datos enviados a un diccionario
    try:
        cliente_actualizado = ClienteController.actualizar_cliente(id, datos)
        if cliente_actualizado:
            return JsonResponse(cliente_actualizado.to_dict())
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Eliminar un cliente por su ID
@require_http_methods(["DELETE"])
def eliminar_cliente(request, id):
    try:
        eliminado = ClienteController.eliminar_cliente(id)
        if eliminado:
            return JsonResponse({'mensaje': 'Cliente eliminado correctamente'})
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
