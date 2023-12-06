from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        exclude = ('created_on' , 'updated_on',)