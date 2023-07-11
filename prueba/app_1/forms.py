from django import forms
from .models import MensajeContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ('nombre', 'email', 'asunto', 'mensaje')
        
        widgets = {
            'nombre': forms.TextInput(attrs={
                               'placeholder': 'Ingrese su nombre',
                               'class': 'form-control'
                           }),
            'email': forms.EmailInput(attrs={
                               'placeholder': 'Ingrese su e-mail',
                               'class': 'form-control'
                           }),
            'asunto': forms.TextInput(attrs={
                               'placeholder': 'Ingrese su asunto',
                               'class': 'form-control'
                           }),
            'mensaje': forms.Textarea(attrs={
                'placeholder':'Cuentanos tus dudas o preguntas... 😁',
                'class': 'form-control observaciones-field', 'rows': 2})
        }

class FormularioPedido(forms.Form):

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

  id = forms.CharField(widget=forms.HiddenInput(), required=False)

  numero = forms.CharField(label='Número de Pedido', max_length=10, required=True,
                          error_messages={
                            'required': 'El número de pedido es requerido',
                            'max_length': 'El número de pedido no puede superar los 10 caracteres'},
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Pedido'}),
                          help_text='Ingrese el número de pedido')
  fecha = forms.DateField(label="Fecha", required=True,
                          error_messages={
                            'required': 'La fecha es requerida'},
                          widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
                          help_text='Ingrese la fecha del pedido')
  estado = forms.ChoiceField(choices=ESTADOS_CHOICES, required=True,
                            error_messages={'required': 'El estado es requerido'},
                            widget=forms.Select(attrs={'class': 'form-control'}),
                            help_text='Seleccione el estado del pedido')
  forma_pago = forms.ChoiceField(choices=PAGOS_CHOICES, required=True,
                                error_messages={'required': 'La forma de pago es requerida'},
                                widget=forms.Select(attrs={'class': 'form-control'}),
                                help_text='Seleccione la forma de pago del pedido')

class FormularioDetallePedido(forms.Form):

  id = forms.CharField(widget=forms.HiddenInput(), required=False)
  producto = forms.ChoiceField(choices=[], required=True,
                            error_messages={'required': 'El producto es requerido'},
                            widget=forms.Select(attrs={'class': 'form-control'}),
                            help_text='Seleccione el producto')
  cantidad = forms.IntegerField(label='Cantidad', required=True,
                                error_messages={
                                  'required': 'La cantidad es requerida'},
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
                                help_text='Ingrese la cantidad')
  precio = forms.DecimalField(label='Precio', required=True,
                              error_messages={
                                'required': 'El precio es requerido'},
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
                              help_text='Ingrese el precio')
  total = forms.DecimalField(label='Total', required=True,
                            error_messages={
                              'required': 'El total es requerido'},
                            widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
                            help_text='Ingrese el total')