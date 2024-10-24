from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente,Vehiculo,Facturacion,FacturacionDetalle,Rastreo,Ubicacion,Transportista,Envio,Paquete,AsignacionVehiculoTransportista as Asignacion 
from django.contrib import messages


def home(request):
    return render(request, 'home.html')  

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()  
    return render(request, 'asignacion/listar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    #
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

def listar_paquete(request):
    paquetes = Paquete.objects.all()  
    return render(request, 'Paquete/list_paquete.html', {'Paquetes': paquetes})

def crear_paquete(request):
    if request.method=='GET':
        envios=Envio.objects.all()
        return render(request,'Paquete/create_paquete.html',{'Envios': envios,})
    if request.method=='POST':
        id_envio=request.POST.get('id_envio')
        descripcion_paquete=request.POST.get('descripcion_paquete')
        peso=request.POST.get('peso')
        dimensiones=request.POST.get('dimensiones')
        valor_declarado=request.POST.get('valor_declarado')

        nuevo_paquete= Paquete(
            id_envio,
            descripcion_paquete,
            peso,
            dimensiones,
            valor_declarado
        )
        nuevo_paquete.save()
        return redirect('list_paquete')
    #Actualizar paquete
def actualizar_paquete(request, id):
    paquete = get_object_or_404(Paquete, id=id) 
    if request.method == 'GET':
        return render(request, 'Paquete/update_paquete.html', {'paquete': paquete})
    
    if request.method == 'POST':
        descripcion_paquete = request.POST.get('descripcion_paquete')
        paquete.descripcion_paquete = descripcion_paquete
        paquete.save()

        messages.success(request, "El paquete ha sido actualizado correctamente.")
        return redirect('list_paquete')

def listar_envios(request):
    envios=Envio.objects.all()
    return render (request,'envios/listar_envios.html',{'envios':envios})
def crear_envio(request):
    if request.method == 'GET':
        asignaciones = Asignacion.objects.all() 
        ubicaciones = Ubicacion.objects.all()    
        return render(request, 'envios/create_envio.html', {
            'asignaciones': asignaciones,
            'ubicaciones': ubicaciones
        })
    if request.method == 'POST':
        try:
            id_asignacion = request.POST.get('asignacion')
            id_ubicacion = request.POST.get('ubicacion')
            estado_envio = request.POST.get('estado')
            codigo_rastreo = request.POST.get('rastreo')

            nuevo_envio = Envio(
                id_asignacion=id_asignacion,
                id_ubicacion=id_ubicacion,
                estado_envio=estado_envio,
                codigo_rastreo=codigo_rastreo
            )

            nuevo_envio.save()
            messages.success(request, "El envio ha sido creado exitosamente.")
            return redirect('listar_envios')
        except Exception as e:
            messages.error(request, f"Error al crear el envio: {e}")
            return render(request, 'envios/create_envio.html')
    
def actualizar_envio(request, id):
    envio = get_object_or_404(Envio, id=id)  
    if request.method == 'GET':
       
        return render(request, 'envios/update_envio.html', {'envio': envio})
    if request.method == 'POST':
       
        estado_envio = request.POST.get('estado')
        envio.estado_envio = estado_envio
        envio.save()  
        messages.success(request, "El estado del envio ha sido actualizado.")
        return redirect('listar_envios')
