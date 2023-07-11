from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', VistaLoginCustom.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('acerca_de/', views.nosotros, name='acerca_de'),
   path('contacto/', views.contacto, name='contacto'),
   path('tienda/', views.tienda, name='tienda'),
   path('producto/', views.producto, name='producto'),
   path('perfil_usuario/', views.perfil_usuario, name='perfil'),
   path('exito', views.exito, name='exito'),
]