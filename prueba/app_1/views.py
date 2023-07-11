from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioContacto
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'acerca-de.html')

def tienda(request):
    return render(request, 'tienda.html')

def producto(request):
    return render(request, 'producto.html')

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


    

    