from django.shortcuts import render, redirect,get_object_or_404
from .models import Cliente,Vehiculo,Facturacion,FacturacionDetalle,Rastreo,Ubicacion,Transportista,Envio,Paquete,AsignacionVehiculoTransportista as Asignacion 
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')  
def contactos(request):
    return render(request,'contacto.html')
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all().filter(activo=True)  
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method=='GET':
        return render(request,'vehiculo/create_vehiculo.html')
    if request.method=='POST':
        matricula_vehiculo=request.POST.get('matricula')
        marca_vehiculo=request.POST.get('marca')
        modelo_vehiculo=request.POST.get('modelo')

        nuevo_vehiculo= Vehiculo(
            matricula_vehiculo=matricula_vehiculo,
            marca_vehiculo=marca_vehiculo,
            modelo_vehiculo=modelo_vehiculo
        )
        nuevo_vehiculo.save()

        return redirect('listar_vehiculos')
def actualizar_vehiculo(request,id_vehiculo):
    vehiculo=get_object_or_404(Vehiculo,id_vehiculo=id_vehiculo)
    if request.method=='GET':
        return render(request,'vehiculo/update_vehiculo.html',{'vehiculo': vehiculo})
    if request.method=='POST':
       
        matricula_vehiculo=request.POST.get('matricula')
        marca_vehiculo=request.POST.get('marca')
        modelo_vehiculo=request.POST.get('modelo')

        vehiculo.matricula_vehiculo=matricula_vehiculo
        vehiculo.marca_vehiculo=marca_vehiculo
        vehiculo.modelo_vehiculo=modelo_vehiculo
        
        vehiculo.save()
        return redirect('listar_vehiculos')

def eliminar_vehiculo(request,id_vehiculo):
    vehiculo=get_object_or_404(Vehiculo,id_vehiculo=id_vehiculo)
    if request.method=='GET':
        return render(request,'vehiculo/confirmar_eliminacion.html',{'vehiculo':vehiculo})
    
    if request.method=='POST':
        vehiculo.activo=False
        vehiculo.save()
        return redirect('listar_vehiculos')
def listar_asignaciones(request):
    asignaciones = Asignacion.objects.select_related('id_vehiculo', 'id_transportista').all().filter(activo=True)
    return render(request, 'asignacion/listar_asignaciones.html', {'asignaciones': asignaciones})

def crear_asignacion(request):
    transportistas=Transportista.objects.all().filter(activo=True)
    vehiculos=Vehiculo.objects.all().filter(activo=True)
    if request.method == 'GET':
        return render(request, 'asignacion/create_asignacion.html',{
            'transportistas':transportistas,
            'vehiculos': vehiculos
        })

    if request.method == 'POST':
        id_transportista = request.POST.get('transportista')
        id_vehiculo=request.POST.get('vehiculo')
        fecha_fin_asignacion=request.POST.get('fecha_fin')
        transportista=get_object_or_404(Transportista,id_transportista=id_transportista)
        vehiculo=get_object_or_404(Vehiculo,id_vehiculo=id_vehiculo)
        nueva_asignacion = Asignacion(
            id_transportista=transportista,
            id_vehiculo=vehiculo,
            fecha_fin_asignacion=fecha_fin_asignacion
        )
        
        nueva_asignacion.save()

        return redirect('listar_asignaciones')  
def actualizar_asignacion(request,id_asignacion):
    asignacion=get_object_or_404(Asignacion,id_asignacion=id_asignacion)
    if request.method=='GET':
        return render(request,'asignacion/update_asignacion.html',{
            'asignacion':asignacion,
            'transportistas': Transportista.objects.all().filter(activo=True),
            'vehiculos': Vehiculo.objects.all().filter(activo=True)
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
    tranportistas=Transportista.objects.all().filter(activo=True)
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
            return redirect('listar_transportistas')
        except Exception as e:
            messages.error(request, f"Error al crear el transportista: {e}")
            return render(request, 'transportista/create_transportista.html')

def actualizar_transportista(request,id_transportista):
    transportista=get_object_or_404(Transportista,id_transportista=id_transportista)
    if request.method=='GET':
        return render(request,'transportista/update_transportista.html',{'transportista':transportista})
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
def eliminar_transportista(request, id_transportista):
    transportista = get_object_or_404(Transportista, id_transportista=id_transportista)
    if request.method=='GET':
        return render(request, 'transportista/confirmar_eliminacion.html', {'transportista': transportista})
    if request.method == 'POST':
        transportista.activo = False
        transportista.save()
        return redirect('listar_transportistas')

   
def listar_rastreo(request):
    try:
        rastreos = Rastreo.objects.exclude(estado_paquete='Entregado')
        return render(request,'rastreo/listar_rastreos.html',{'rastreos':rastreos})
    except Exception as e:
        messages.error(request,f'Error al listar rastreo : {e}')
def crear_rastreo(request):
    envios = Envio.objects.exclude(estado_envio='cancelado')
    if request.method == 'GET':
        return render(request, 'rastreo/create_rastreo.html', {
            'envios': envios,
            'rastreo': Rastreo
        })
    if request.method == 'POST':
        try:
            id_envio = request.POST.get('envio')
            ubicacion_actual = request.POST.get('ubicacion')
            observaciones = request.POST.get('observaciones')
            envio=get_object_or_404(Envio,id_envio=id_envio)
            nuevo_rastreo = Rastreo(
                id_envio=envio,
                ubicacion_actual=ubicacion_actual,
                observaciones=observaciones
            )
            nuevo_rastreo.save()
            return redirect('listar_rastreos')
        except Exception as e:
            messages.error(request, f'Error: {e}')
def actualizar_rastreo(request,id_rastreo):
    rastreo=get_object_or_404(Rastreo,id_rastreo=id_rastreo)
    if request.method=='GET':
        return render(request,'rastreo/update_rastreo.html',{'rastreo':rastreo})
    if request.method=='POST':
        try:
            ubicacion_actual=request.POST.get('ubicacion')
            estado_paquete=request.POST.get('estado')

            rastreo.ubicacion_actual=ubicacion_actual
            rastreo.estado_paquete=estado_paquete

            rastreo.save()
            return redirect('listar_rastreos')
        except Exception as e:
            messages.error(request,f'Error al actualizar el rastreo: {e}')

def listar_paquetes(request):
    paquetes = Paquete.objects.all()
    return render(request, 'paquete/listar_paquetes.html', {'Paquetes': paquetes})

def crear_paquete(request):
    if request.method=='GET':
        envios=Envio.objects.all().filter(estado_envio='pendiente')
        return render(request,'paquete/create_paquete.html',{'Envios': envios})
    if request.method=='POST':
        id_envio=request.POST.get('id_envio')
        descripcion_paquete=request.POST.get('descripcion_paquete')
        peso=request.POST.get('peso')
        dimensiones=request.POST.get('dimensiones')
        valor_declarado=request.POST.get('valor_declarado')
        envio=get_object_or_404(Envio,id_envio=id_envio)
        nuevo_paquete= Paquete(
            id_envio=envio,
            descripcion_paquete=descripcion_paquete,
            peso=peso,
            dimensiones=dimensiones,
            valor_declarado=valor_declarado,
            asignado=True
        )
        nuevo_paquete.save()
        return redirect('listar_paquetes')
def actualizar_paquete(request, id_paquete):
    paquete = get_object_or_404(Paquete, id_paquete=id_paquete)

    if request.method == 'GET':
        return render(request, 'paquete/editar_paquete.html', {'paquete': paquete})

    if request.method == 'POST':
        try:
            descripcion_paquete = request.POST.get('descripcion_paquete')
            peso = request.POST.get('peso')
            dimensiones = request.POST.get('dimensiones')
            valor_declarado = request.POST.get('valor_declarado')

            if not descripcion_paquete:
                raise ValueError("La descripción del paquete es obligatoria.")

            paquete.descripcion_paquete = descripcion_paquete
            paquete.peso = peso
            paquete.dimensiones = dimensiones
            paquete.valor_declarado = valor_declarado

            paquete.save()
            return redirect('listar_paquetes')
        except Exception as e:
            messages.error(request, f'Error al actualizar el paquete: {e}')
            return render(request, 'paquete/editar_paquete.html', {'paquete': paquete})

def listar_envios(request):
    envios=Envio.objects.all()
    return render (request,'envio/listar_envios.html',{'envios':envios})

def crear_envio(request):
    if request.method == 'GET':
        asignaciones = Asignacion.objects.all() 
        ubicaciones = Ubicacion.objects.all()    
        return render(request, 'envio/create_envio.html', {
            'asignaciones': asignaciones,
            'ubicaciones': ubicaciones,
            'Envio':Envio
        })
    if request.method == 'POST':
        try:
            id_asignacion = request.POST.get('asignacion')
            id_ubicacion = request.POST.get('ubicacion')
            estado_envio = request.POST.get('estado')

            asignacion=get_object_or_404(Asignacion,id_asignacion=id_asignacion)
            ubicacion=get_object_or_404(Ubicacion,id_ubicacion=id_ubicacion)
            nuevo_envio = Envio(
                id_asignacion=asignacion,
                id_ubicacion=ubicacion,
                estado_envio=estado_envio,
            )

            nuevo_envio.save()
            return redirect('listar_envios')
        except Exception as e:
            messages.error(request, f"Error al crear el envio: {e}")
            return render(request, 'envio/create_envio.html')
    
def actualizar_envio(request, id_envio):
    envio = get_object_or_404(Envio, id_envio=id_envio)  
    if request.method == 'GET':
        return render(request, 'envio/update_envio.html', {
            'envio': envio,
            'Envio':Envio
        })
    if request.method == 'POST':
        estado_envio = request.POST.get('estado')
        envio.estado_envio = estado_envio
        envio.save()  
        return redirect('listar_envios')


def listar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'ubicacion/listar_ubicaciones.html', {'ubicaciones': ubicaciones})

def crear_ubicacion(request):
    clientes=Cliente.objects.all()
    if request.method=='GET':
        return render(request, 'ubicacion/create_ubicacion.html',{'clientes':clientes})
    if request.method == 'POST':
        calle = request.POST.get('calle')
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('postal')
        id_cliente=request.POST.get('cliente')
        referencias=request.POST.get('referencias')
        coordenadas_geograficas=request.POST.get('coordenadas')

        cliente=get_object_or_404(Cliente,id_cliente=id_cliente)
        nueva_ubicacion = Ubicacion(
            calle=calle,
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            referencias=referencias,
            id_cliente=cliente,           
            coordenadas_geograficas=coordenadas_geograficas
        )
        nueva_ubicacion.save()
        return redirect('listar_ubicaciones')  

def actualizar_ubicacion(request, id_ubicacion):
    ubicacion = get_object_or_404(Ubicacion, id_ubicacion=id_ubicacion)  
    if request.method=='GET':
        return render(request, 'ubicacion/update_ubicacion.html', {'ubicacion': ubicacion})
    if request.method == 'POST':
        ubicacion.referencias=request.POST.get('referencias')
        ubicacion.save()  
        return redirect('listar_ubicaciones')

def listar_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'cliente/listar_clientes.html',{'clientes':clientes})
def crear_cliente(request):
    if request.method=='GET':
        return render(request,'cliente/create_cliente.html')
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        telefono=request.POST.get('telefono')

        nuevo_cliente=Cliente(
            nombre=nombre,
            telefono=telefono
        )
        nuevo_cliente.save()
        return redirect('listar_clientes')
def actualizar_cliente(request,id_cliente):
    cliente=get_object_or_404(Cliente,id_cliente=id_cliente)
    if request.method=='GET':
        return render(request,'cliente/update_cliente.html',{'cliente':cliente})
    if request.method=='POST':
        telefono=request.POST.get('telefono')
        nombre=request.POST.get('nombre')
        cliente.telefono=telefono
        cliente.nombre=nombre
        cliente.save()
        return redirect('listar_clientes')
    
def listar_facturas(request):
    facturas = Facturacion.objects.all()
    return render(request, 'facturacion/listar_facturas.html', {'facturas': facturas})

def crear_factura(request):
    if request.method=='GET':
        clientes = Cliente.objects.all()
        return render(request, 'facturacion/create_facturacion.html', {'clientes': clientes})
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')

        cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
        nueva_factura = Facturacion(
            id_cliente=cliente
        )
        nueva_factura.save()
        return redirect('crear_factura_detalle',factura_id=nueva_factura.id_factura)

def listar_factura_detalle(request):
    detalles = FacturacionDetalle.objects.all()
    return render(request, 'facturacion_detalle/listar_facturas_detalles.html', {'detalles': detalles})

def crear_factura_detalle(request, factura_id):
    factura = get_object_or_404(Facturacion, id_factura=factura_id)
    metodo_pago_choices = FacturacionDetalle._meta.get_field('metodo_pago').choices
    if request.method == 'GET':
        return render(request, 'facturacion_detalle/create_factura_detalle.html', {
            'factura': factura,
            'metodo_pago_choices': metodo_pago_choices
        })
    if request.method == 'POST':
        monto = request.POST.get('monto')
        metodo_pago = request.POST.get('metodo')

        nuevo_detalle = FacturacionDetalle(
            id_factura=factura,
            monto_total=monto,
            metodo_pago=metodo_pago
        )
        nuevo_detalle.save()
        return redirect('listar_factura_detalle')
    
@csrf_exempt
def buscar_envio(request):
    if request.method == 'GET':
        return render(request, 'envio/consultar.html')
    elif request.method == 'POST':
        codigo = request.POST.get('codigo')
        envio = None
        rastreo = None  
        if codigo:
            envio = Envio.objects.filter(codigo_rastreo=codigo).select_related('id_asignacion', 'id_ubicacion').first()
            if envio: 
                rastreo = Rastreo.objects.filter(id_envio=envio.id_envio)
        return render(request, 'envio/resultado_envio.html', {
            'envio': envio,
            'rastreo': rastreo
        })
