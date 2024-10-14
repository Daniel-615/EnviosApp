from django.http import JsonResponse
from ..controllers import PaqueteController

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
