from django.db import models
import uuid

class Cliente(models.Model):
    id_cliente = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    nombre = models.CharField(
        max_length=30, blank=False, null=False
    )
    telefono= models.CharField(
        max_length=20, blank=False, null=False,
    )
    
    
    class Meta:
        indexes = [models.Index(fields=['telefono'])]

    def __str__(self):
        return f'{self.remitente} -> {self.destinatario}'


class Transportista(models.Model):
    id_transportista = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    nombre_transportista = models.CharField(
        max_length=40, blank=False, null=False
    )
    apellido_transportista = models.CharField(
        max_length=40, blank=False, null=False
    )
    dpi_transportista = models.CharField(
        max_length=15, blank=False, null=False,
    )
    licencia_transportista = models.CharField(
        max_length=15, blank=False, null=False,
    )
    correo_transportista = models.EmailField(
        max_length=100, blank=False, null=False
    )
    telefono_transportista = models.CharField(
        max_length=15, blank=False, null=False,
    )
    activo=models.BooleanField(
        default=True
    )
    class Meta:
        indexes = [models.Index(fields=['telefono_transportista']), models.Index(fields=['dpi_transportista'])]

    def __str__(self):
        return f'{self.nombre_transportista} {self.apellido_transportista}'


class Vehiculo(models.Model):
    id_vehiculo = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    matricula_vehiculo = models.CharField(
        max_length=20, blank=False, null=False
    )
    marca_vehiculo = models.CharField(
        max_length=40, blank=False, null=False
    )
    modelo_vehiculo = models.CharField(
        max_length=40, blank=False, null=False
    )
    activo=models.BooleanField(
        default=True
    )
    def __str__(self):
        return f'vehículo: {self.modelo_vehiculo}'


class AsignacionVehiculoTransportista(models.Model):
    id_asignacion = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_transportista = models.ForeignKey(
        Transportista, on_delete=models.CASCADE, related_name='transportista'
    )
    id_vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, related_name='vehiculo'
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_fin_asignacion = models.DateTimeField(
        null=True, blank=True
    )
    activo=models.BooleanField(
        default=True
    )
    def __str__(self):
        return f'{self.id_transportista} asignado a {self.id_vehiculo} desde {self.fecha_asignacion}'


class Ubicacion(models.Model):
    id_ubicacion = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='cliente'
    )
    ciudad = models.CharField(
        max_length=100, blank=False, null=False
    )
    calle = models.CharField(
        max_length=150, blank=False, null=False
    )
    codigo_postal = models.CharField(
        max_length=10, blank=False, null=False,
    )
    coordenadas_geograficas = models.CharField(
        max_length=255,blank=False,null=False
    )
    referencias = models.TextField(
        blank=False, null=False
    )  

    def __str__(self):
        return f'{self.ciudad}, {self.calle}'


class Envio(models.Model):
    id_envio = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_asignacion = models.ForeignKey(
        AsignacionVehiculoTransportista, on_delete=models.CASCADE, related_name='asignacion'
    )
    id_ubicacion = models.ForeignKey(
        Ubicacion, on_delete=models.CASCADE, related_name='ubicacion'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En tránsito'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ]
    estado_envio = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )
    codigo_rastreo = models.CharField(
        max_length=36, unique=True, editable=False
    )

    def save(self, *args, **kwargs):
        if not self.codigo_rastreo:
            self.codigo_rastreo = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Envío creado {self.codigo_rastreo}'


class Paquete(models.Model):
    id_paquete = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_envio = models.ForeignKey(
        Envio, on_delete=models.CASCADE, related_name='paquetes'
    )
    descripcion_paquete = models.CharField(
        max_length=255
    )
    peso = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    dimensiones = models.CharField(
        max_length=100
    )
    valor_declarado = models.DecimalField(
        max_digits=12, decimal_places=2
    )
    asignado=models.BooleanField(
        default=False
    )
    def __str__(self):
        return f"Paquete {self.id_paquete} - {self.descripcion_paquete}"


class Rastreo(models.Model):
    id_rastreo = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_envio = models.ForeignKey(
        Envio, on_delete=models.CASCADE, related_name='rastreos'
    )
    ubicacion_actual = models.CharField(max_length=255,blank=False,null=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    ESTADO_CHOICES = [
        ('en_transito', 'En tránsito'),
        ('en_almacen', 'En almacén'),
        ('entregado', 'Entregado'),
        ('demorado', 'Demorado'),
        ('cancelado', 'Cancelado')
    ]
    estado_paquete = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES,
        default='en_transito'
    )
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rastreo {self.id_rastreo} - {self.id_envio} - {self.estado_paquete} - {self.ubicacion_actual}"


class Facturacion(models.Model):
    id_factura = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Factura {self.id_factura}'


class FacturacionDetalle(models.Model):
    id_factura_detalle = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    id_factura = models.ForeignKey(
        Facturacion, on_delete=models.CASCADE, related_name='detalles'
    )
    monto_total = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    fecha_facturacion = models.DateTimeField(auto_now_add=True)
    PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('contra entrega', 'Contra Entrega'),
    ]
    metodo_pago = models.CharField(
        max_length=50, choices=PAGO_CHOICES, blank=False, null=False
    )

    def __str__(self):
        return f'Detalle de Factura {self.id_factura_detalle}'
