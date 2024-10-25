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

#UBICACION
def listar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'ubicacion/list_ubicacion.html', {'ubicaciones': ubicaciones})

def crear_ubicacion(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')

        # Crear una nueva instancia del modelo Ubicacion
        nueva_ubicacion = Ubicacion(
            direccion=direccion,
            ciudad=ciudad,
            pais=pais
        )
        nueva_ubicacion.save()
        messages.success(request, "La ubicación ha sido creada exitosamente.")
        return redirect('listar_ubicaciones')  
    return render(request, 'ubicacion/create_ubicacion.html')

def actualizar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)  

    if request.method == 'POST':
        ubicacion.direccion = request.POST.get('direccion')
        ubicacion.ciudad = request.POST.get('ciudad')
        ubicacion.pais = request.POST.get('pais')
        ubicacion.save()  # Guardar los cambios

        messages.success(request, "La ubicación ha sido actualizada exitosamente.")
        return redirect('listar_ubicaciones')
    return render(request, 'ubicacion/update_ubicacion.html', {'ubicacion': ubicacion})

def eliminar_ubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)

    if request.method == 'POST':
        ubicacion.delete()  # Eliminar la ubicación
        messages.success(request, "La ubicación ha sido eliminada exitosamente.")
        return redirect('listar_ubicaciones')  # Redirigir a la lista de ubicaciones
    # Confirmación antes de eliminar
    return render(request, 'ubicacion/delete_ubicacion.html', {'ubicacion': ubicacion})


#FACTURA
def crear_factura(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        fecha = request.POST.get('fecha')
        total = request.POST.get('total')

        nueva_factura = Facturacion(
            cliente_id=cliente_id,
            fecha=fecha,
            total=total
        )
        nueva_factura.save()
        messages.success(request, "La factura ha sido creada exitosamente.")
        return redirect('listar_facturas')

    clientes = Cliente.objects.all()
    return render(request, 'factura/create_factura.html', {'clientes': clientes})

def listar_facturas(request):
    facturas = Facturacion.objects.all()
    return render(request, 'factura/list_facturas.html', {'facturas': facturas})

def actualizar_factura(request, id):
    factura = get_object_or_404(Facturacion, id=id)

    if request.method == 'POST':
        factura.cliente_id = request.POST.get('cliente')
        factura.fecha = request.POST.get('fecha')
        factura.total = request.POST.get('total')
        factura.save()

        messages.success(request, "La factura ha sido actualizada exitosamente.")
        return redirect('listar_facturas')

    clientes = Cliente.objects.all()
    return render(request, 'factura/update_factura.html', {'factura': factura, 'clientes': clientes})

#FACTURA DETALLE
def crear_factura_detalle(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        descripcion = request.POST.get('descripcion')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')

        nuevo_detalle = FacturacionDetalle(
            factura_id=factura_id,
            descripcion=descripcion,
            cantidad=cantidad,
            precio=precio
        )
        nuevo_detalle.save()
        messages.success(request, "El detalle de la factura ha sido creado exitosamente.")
        return redirect('listar_factura_detalle')

    facturas = Facturacion.objects.all()
    return render(request, 'factura/create_factura_detalle.html', {'facturas': facturas})

def listar_factura_detalle(request):
    detalles = FacturacionDetalle.objects.all()
    return render(request, 'factura/list_factura_detalle.html', {'detalles': detalles})

def actualizar_factura_detalle(request, id):
    detalle = get_object_or_404(FacturacionDetalle, id=id)

    if request.method == 'POST':
        detalle.factura_id = request.POST.get('factura')
        detalle.descripcion = request.POST.get('descripcion')
        detalle.cantidad = request.POST.get('cantidad')
        detalle.precio = request.POST.get('precio')
        detalle.save()

        messages.success(request, "El detalle de la factura ha sido actualizado exitosamente.")
        return redirect('listar_factura_detalle')

    facturas = Facturacion.objects.all()
    return render(request, 'factura/update_factura_detalle.html', {'detalle': detalle, 'facturas': facturas})


#ELIMINAR 
def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, "El vehículo ha sido eliminado exitosamente.")
        return redirect('listar_vehiculos')
    
    return render(request, 'asignacion/delete_vehiculo.html', {'vehiculo': vehiculo})

def eliminar_asignacion(request, id):
    asignacion = get_object_or_404(Asignacion, id=id)
    
    if request.method == 'POST':
        asignacion.delete()
        messages.success(request, "La asignación ha sido eliminada exitosamente.")
        return redirect('listar_asignaciones')
    
    return render(request, 'asignacion/delete_asignacion.html', {'asignacion': asignacion})

def eliminar_transportista(request, id):
    transportista = get_object_or_404(Transportista, id=id)
    
    if request.method == 'POST':
        transportista.delete()
        messages.success(request, "El transportista ha sido eliminado exitosamente.")
        return redirect('listar_transportistas')
    
    return render(request, 'transportista/delete_transportista.html', {'transportista': transportista})

def eliminar_paquete(request, id):
    paquete = get_object_or_404(Paquete, id=id)
    
    if request.method == 'POST':
        paquete.delete()
        messages.success(request, "El paquete ha sido eliminado exitosamente.")
        return redirect('listar_paquetes')
    
    return render(request, 'paquete/delete_paquete.html', {'paquete': paquete})

def eliminar_envio(request, id):
    envio = get_object_or_404(Envio, id=id)
    
    if request.method == 'POST':
        envio.delete()
        messages.success(request, "El envío ha sido eliminado exitosamente.")
        return redirect('listar_envios')
    
    return render(request, 'envios/delete_envio.html', {'envio': envio})

def eliminar_factura(request, id):
    factura = get_object_or_404(Facturacion, id=id)
    
    if request.method == 'POST':
        factura.delete()
        messages.success(request, "La factura ha sido eliminada exitosamente.")
        return redirect('listar_facturas')
    
    return render(request, 'factura/delete_factura.html', {'factura': factura})

def eliminar_factura_detalle(request, id):
    detalle = get_object_or_404(FacturacionDetalle, id=id)
    
    if request.method == 'POST':
        detalle.delete()
        messages.success(request, "El detalle de la factura ha sido eliminado exitosamente.")
        return redirect('listar_factura_detalle')
    
    return render(request, 'factura/delete_factura_detalle.html', {'detalle': detalle})
