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
