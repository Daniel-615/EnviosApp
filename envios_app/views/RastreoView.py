from django.http import JsonResponse
from ..controllers import RastreoController

# Listar rastreos
def listar_rastreos(request):
    rastreos = RastreoController.obtener_Rastreo()
    data = list(rastreos.values())
    return JsonResponse(data, safe=False)

# Obtener rastreo por ID
def obtener_rastreo(request, id):
    rastreo = RastreoController.obtener_rastreo_id(id)
    if rastreo:
        return JsonResponse(rastreo.to_dict())
    return JsonResponse({'error': 'Rastreo no encontrado'}, status=404)

# Crear un nuevo rastreo
def crear_rastreo(request):
    if request.method == 'POST':
        envio = request.POST.get('envio')
        ubicacion_actual = request.POST.get('ubicacion_actual')
        estado = request.POST.get('estado', 'en_transito')
        observaciones = request.POST.get('observaciones', '')
        rastreo = RastreoController.crear_rastreo(envio, ubicacion_actual, estado, observaciones)
        return JsonResponse(rastreo.to_dict(), status=201)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
