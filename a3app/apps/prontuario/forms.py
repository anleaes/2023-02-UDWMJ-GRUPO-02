from django import forms
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):

    class Meta:
        model = Prontuario
        exclude = ('created_on' , 'updated_on',)