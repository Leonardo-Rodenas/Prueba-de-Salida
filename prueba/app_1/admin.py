from django.contrib import admin
from .models import MensajeContacto, Producto, Productor, Cliente

# Register your models here.

admin.site.register(MensajeContacto)
admin.site.register(Producto)
admin.site.register(Productor)
admin.site.register(Cliente)
