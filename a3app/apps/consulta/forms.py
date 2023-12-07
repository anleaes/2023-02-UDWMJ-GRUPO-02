from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        exclude = ('created_on', 'updated_on',)