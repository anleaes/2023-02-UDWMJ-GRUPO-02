from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ('created_on' , 'updated_on')