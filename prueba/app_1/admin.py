from django.contrib import admin
from .models import MensajeContacto, Producto, Productor, Cliente, Pedido, DetallePedido

# Register your models here.

admin.site.register(MensajeContacto)
admin.site.register(Producto)
admin.site.register(Productor)
admin.site.register(Cliente)
admin.site.register(DetallePedido)
admin.site.register(Pedido)