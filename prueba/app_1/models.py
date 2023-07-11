from django.db import models

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
    
