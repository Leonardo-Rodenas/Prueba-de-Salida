from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from app_1.views import PedidoView, PedidoEliminarView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', VistaLoginCustom.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('acerca_de/', views.nosotros, name='acerca_de'),
   path('contacto/', views.contacto, name='contacto'),
   path('tienda/', views.tienda, name='tienda'),
   path('producto/<idProducto>', views.producto, name='producto'),
   path('perfil_usuario/', views.perfil_usuario, name='perfil'),
   path('exito', views.exito, name='exito'),
   path('pedidos/', PedidoView.as_view(), name='pedidos'),
   path('pedidos/<int:pk>/delete/', PedidoEliminarView.as_view(), name='pedido_eliminar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)