from django.http import JsonResponse
from ..controllers.PaqueteController import PaqueteController

# Listar paquetes
def listar_paquetes(request):
    paquetes = PaqueteController.obtener_paquetes()
    data = list(paquetes.values())
    return JsonResponse(data, safe=False)

# Obtener paquete por ID
def obtener_paquete(request, id):
    paquete = PaqueteController.obtener_paquete_id(id)
    if paquete:
        return JsonResponse(paquete.to_dict())
    return JsonResponse({'error': 'Paquete no encontrado'}, status=404)

# Crear un nuevo paquete
def crear_paquete(request):
    if request.method == 'POST':
        envio = request.POST.get('envio')
        descripcion = request.POST.get('descripcion')
        peso = request.POST.get('peso')
        dimensiones = request.POST.get('dimensiones')
        valor = request.POST.get('valor')
        paquete = PaqueteController.crear_paquete(envio, descripcion, peso, dimensiones, valor)
        return JsonResponse(paquete.to_dict(), status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Actualizar un paquete existente
def actualizar_paquete(request, id):
    if request.method == 'PUT':
        envio = request.PUT.get('envio')
        descripcion = request.PUT.get('descripcion')
        peso = request.PUT.get('peso')
        dimensiones = request.PUT.get('dimensiones')
        valor = request.PUT.get('valor')
        paquete_actualizado = PaqueteController.actualizar_paquete(id, envio, descripcion, peso, dimensiones, valor)
        if paquete_actualizado:
            return JsonResponse(paquete_actualizado.to_dict())
        return JsonResponse({'error': 'Paquete no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Eliminar un paquete
def eliminar_paquete(request, id):
    if request.method == 'DELETE':
        paquete_eliminado = PaqueteController.eliminar_paquete(id)
        if paquete_eliminado:
            return JsonResponse({'mensaje': 'Paquete eliminado correctamente'}, status=200)
        return JsonResponse({'error': 'Paquete no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
