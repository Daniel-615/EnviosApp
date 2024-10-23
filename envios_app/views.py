from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente,Vehiculo,Facturacion,FacturacionDetalle,Rastreo,Ubicacion,Transportista,Envio,Paquete,AsignacionVehiculoTransportista as Asignacion 
from django.contrib import messages


def home(request):
    return render(request, 'home.html')  

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
def listar_transportistas(request):
    tranportistas=Transportista.objects.all()
    return render(request,'transportista/listar_transportistas.html',{'transportistas':tranportistas})
def crear_transportista(request):
    if request.method=='GET':
        return render(request,'transportista/create_transportista.html')
    if request.method=='POST':
        try:
            nombre_transportista=request.POST.get('nombre')
            apellido_transportista=request.POST.get('apellido')
            dpi_transportista=request.POST.get('dpi')
            licencia_transportista=request.POST.get('licencia')
            correo_transportista=request.POST.get('correo')
            telefono_transportista=request.POST.get('telefono')

            nuevo_transportista=Transportista(
                nombre_transportista=nombre_transportista,
                apellido_transportista=apellido_transportista,
                dpi_transportista=dpi_transportista,
                licencia_transportista=licencia_transportista,
                correo_transportista=correo_transportista,
                telefono_transportista=telefono_transportista
            )

            nuevo_transportista.save()
            messages.success(request, "El transportista ha sido creado exitosamente.")
            return redirect('listar_transportistas')
        except Exception as e:
            messages.error(request, f"Error al crear el transportista: {e}")
            return render(request, 'transportista/create_transportista.html')

def actualizar_transportista(request,id):
    transportista=get_object_or_404(Transportista,id)
    if request.method=='GET':
        return render('transportista/update_transportista.html')
    if request.method=='POST':
        nombre_transportista=request.POST.get('nombre')
        apellido_transportista=request.POST.get('apellido')
        dpi_transportista=request.POST.get('dpi')
        licencia_transportista=request.POST.get('licencia')
        correo_transportista=request.POST.get('correo')
        telefono_transportista=request.POST.get('telefono')

        transportista.nombre_transportista=nombre_transportista
        transportista.apellido_transportista=apellido_transportista
        transportista.dpi_transportista=dpi_transportista
        transportista.licencia_transportista=licencia_transportista
        transportista.correo_transportista=correo_transportista
        transportista.telefono_transportista=telefono_transportista

        transportista.save()
        return redirect('listar_transportistas')
