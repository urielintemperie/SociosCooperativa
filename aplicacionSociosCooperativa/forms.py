from django import forms
from .models import Socio
from .models import Pago
from .models import Importe

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ('documento', 'nombre', 'apellido', 'correo', 'curso', 'fechaInscripcion','socioCompleto','usuarioCampus','epecialidad','fechaNacimiento')

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ('socio','fecha', 'pago')

class ImporteForm(forms.ModelForm):
    class Meta:
        model = Importe
        fields = ('fechaInicio', 'fechaFin', 'coste')
