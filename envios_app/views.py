from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente,Vehiculo,Facturacion,FacturacionDetalle,Rastreo,Ubicacion,Transportista,Envio,Paquete,AsignacionVehiculoTransportista as Asignacion 
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()  
    return render(request, 'asignacion/listar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method=='GET':
        return render(request,'asignacion/create_vehiculo.html')
    if request.method=='POST':
        matricula_vehiculo=request.POST.get('matricula')
        marca_vehiculo=request.POST.get('marca')
        modelo_vehiculo=request.POST.get('modelo')

        nuevo_vehiculo= Vehiculo(
            matricula_vehiculo,
            marca_vehiculo,
            modelo_vehiculo
        )
        nuevo_vehiculo.save()

        return redirect('listar_vehiculos')
def actualizar_vehiculo(request,id):
    if request.method=='GET':
        return render(request,'asignacion/update_vehiculo.html')
    if request.method=='POST':
        vehiculo=get_object_or_404(Vehiculo,id)
        matricula_vehiculo=request.POST.get('matricula')
        marca_vehiculo=request.POST.get('marca')
        modelo_vehiculo=request.POST.get('modelo')

        vehiculo.matricula_vehiculo=matricula_vehiculo
        vehiculo.marca_vehiculo=marca_vehiculo
        vehiculo.modelo_vehiculo=modelo_vehiculo
        
        vehiculo.save()
        return redirect('listar_vehiculos')
    
def listar_asignaciones(request):
    asignaciones = Asignacion.objects.all()
    return render(request, 'asignacion/listar_asignaciones.html', {'asignaciones': asignaciones})

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