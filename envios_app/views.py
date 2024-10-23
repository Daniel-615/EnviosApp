from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente,Vehiculo,Facturacion,FacturacionDetalle,Rastreo,Ubicacion,Transportista,Envio,Paquete,AsignacionVehiculoTransportista as Asignacion 

def crear_asignacion(request):
    if request.method == 'GET':
        return render(request, 'asignacion/create_asignacion.html')

    if request.method == 'POST':
        id_transportista = request.POST.get('transportista')
        id_vehiculo=request.POST.get('vehiculo')
        fecha_fin_asignacion=request.POST.GET('fecha_fin')
        
        nueva_asignacion = Asignacion(
            id_transportista,
            id_vehiculo,
            fecha_fin_asignacion
        )
        
        nueva_asignacion.save()

        return redirect('listar_asignaciones')  
def actualizar_asignacion(request,id):
    asignacion=get_object_or_404(Asignacion,id=id)
    if request.method=='GET':
        return render(request,'asignacion/update_asignacion.html',{
            'asignacion':asignacion,
            'transportistas': Transportista.objects.all(),
            'vehiculos': Vehiculo.objects.all()
        })
    if request.method=='POST':
        id_transportista=request.POST.get('transportista')
        id_vehiculo=request.POST.get('vehiculo')
        fecha_fin_asignacion=request.POST.get('fecha_fin')

        asignacion.id_transportista=id_transportista
        asignacion.id_vehiculo=id_vehiculo
        asignacion.fecha_fin_asignacion=fecha_fin_asignacion
        
        asignacion.save()
        return redirect('listar_asignaciones')