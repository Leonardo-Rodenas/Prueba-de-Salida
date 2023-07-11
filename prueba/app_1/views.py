from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioContacto
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Producto, Pedido
from django.views.generic import TemplateView, DeleteView
from app_1.forms import FormularioPedido, FormularioDetallePedido

# Create your views here.

def home(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'acerca-de.html')

def tienda(request):
    return render(request, 'tienda.html')

def producto(request, idProducto):
    produc=Producto.objects.get(idProducto=idProducto)
    return render(request,"producto.html", {"producto":produc})


def contacto(request):
    
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            # Guardar el mensaje de contacto en la base de datos
            mensaje = formulario.save()

            # Enviar correo electrónico
            subject = 'Mensaje de contacto'
            message = f'Nombre: {mensaje.nombre}\nCorreo: {mensaje.email}\nAsunto: {mensaje.asunto}\n\nMensaje:\n{mensaje.mensaje}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            # Mostrar mensaje de éxito
            return render(request, 'exito.html')
    else:
        formulario = FormularioContacto()
    
    return render(request, 'contacto.html', {'formulario': formulario})

# def exito(request):
#     return render(request, 'exito.html')

def perfil_usuario(request):
     return render(request, 'perfil_usuario.html')

def exito(request):
     return render(request, 'exito.html')
 
class VistaLoginCustom(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    
    def get_success_url(self):
        return reverse_lazy('perfil') # Lugar al que se es redirecionado si el login es exitoso

class PedidoView(TemplateView):
  template_name = 'pedidos.html'

  def get(self, request):
    pedidos = Pedido.objects.all()
    return render(request, self.template_name, { 'pedidos': pedidos })

class PedidoEliminarView(DeleteView):
  model = Pedido
  template_name = 'pedido_eliminar.html'
  success_url = reverse_lazy('pedidos')
  
class PedidoCrearView(TemplateView):
  template_name = 'pedido_agregar.html'

  def get(self, request):
    formulario = FormularioPedido()
    return render(request, self.template_name, { 'form': formulario })

  def post(self, request):
    formulario = FormularioPedido(request.POST)
    if formulario.is_valid():
      pedido = Pedido()
      pedido.numero = formulario.cleaned_data['numero']
      pedido.fecha = formulario.cleaned_data['fecha']
      pedido.estado_id = formulario.cleaned_data['estado']
      pedido.forma_pago_id = formulario.cleaned_data['forma_pago']
      pedido.total = 0
      pedido.usuario_id = 1
      pedido.save()
      return redirect('/pedidos/' + str(pedido.id))
      # return render(request, 'pedido_crear.html', { 'form': formulario })
    else:
      return render(request, 'pedido_editar.html', { 'form': formulario })
  
class PedidoEditarView(TemplateView):
  template_name = 'pedido_editar.html'

  def get(self, request, pk):
    form_detalle = FormularioDetallePedido()
    productos = Producto.objects.all().order_by('nombre')
    lista_productos = [(producto.idProducto, producto.nombre) for producto in productos]
    form_detalle.fields['producto'].choices = lista_productos
    form_detalle.fields['id'].initial = pk
    try:
      pedido = Pedido.objects.get(id=pk)
      formulario = FormularioPedido(initial = pedido.__dict__)
    except:
      return render(request, '404.html')
    return render(request, self.template_name, { 'form': formulario, 'pedido': pedido, 'form_detalle': form_detalle })

  def post(self, request, pk):
    formulario = FormularioPedido(request.POST)
    if formulario.is_valid():
      pedido = Pedido.objects.get(id=formulario.cleaned_data['id'])
      pedido.numero = formulario.cleaned_data['numero']
      pedido.fecha = formulario.cleaned_data['fecha']
      pedido.estado_id = formulario.cleaned_data['estado']
      pedido.forma_pago_id = formulario.cleaned_data['forma_pago']
      pedido.save()
    return render(request, 'pedido_editar.html', { 'form': formulario })
