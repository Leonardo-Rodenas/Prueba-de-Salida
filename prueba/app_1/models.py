from django.db import models
from django.utils import timezone

# Create your models here.

# contacto/models.py

from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcionProducto = models.TextField(default='Sin descripcion')
    stockProducto = models.IntegerField()
    precioProducto = models.IntegerField()
    imagProducto = models.ImageField(upload_to='medios', default='medios/not-found.jpg')
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.nombre
    
class Productor(models.Model):
    idProductor = models.AutoField(primary_key=True)
    nombreContacto = models.CharField(max_length=100, null=True, blank=True)
    rut = models.CharField(max_length=15, null=True, blank=True)
    razonSocial = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    comuna = models.CharField(max_length=100, null=True, blank=True)
    rubro = models.CharField(max_length=100, null=True, blank=True)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.nombreContacto
    class Meta:
        verbose_name_plural = "Productores"
        
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=100, null=True, blank=True)
    rut_identificador = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    comuna = models.CharField(max_length=100, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    fono = models.CharField(max_length=100, null=True, blank=True)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.nombreCliente
       
class Pedido(models.Model):
    
    PAGOS_CHOICES = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('Crédito', 'Crédito'),
        ('Debito', 'Debito'),
        ('PayPal', 'PayPal'),
        ('Mach', 'Mach'),
    ]

    VIA_CHOICES = [
        ('Telefono', 'Telefono'),
        ('E-mail', 'E-mail'),
        ('Web', 'Web'),
    ]

    ESTADOS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Preparación', 'En Preparación'),
        ('En Despacho', 'En Despacho'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]
    
    idcliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, default=0)
    metodo_pago = models.CharField(max_length=15, choices=PAGOS_CHOICES, default='Crédito')
    fecha_pedido = models.DateTimeField(default=timezone.now)
    mediopedido = models.CharField(max_length=15, choices=VIA_CHOICES, default='Web')
    estado = models.CharField(max_length=15, choices=ESTADOS_CHOICES, default='Pendiente')
    deleted = models.BooleanField(default=False)
    pedido_staff = models.BooleanField(default=False)
    is_modificable = models.BooleanField(default=True)
    precio_total = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    @property
    def str_nombre(self):
        return f"Pedido N°: {self.id}"

    def __str__(self):
        return self.str_nombre

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    idpedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False,default=1)
    precio = models.IntegerField(null=False)
    deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    @property
    def str_nombre(self):
        return f"{self.id}, {self.idproducto}, {self.precio}"

    def __str__(self):
        return self.str_nombre