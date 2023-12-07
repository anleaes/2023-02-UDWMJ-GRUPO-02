from django import forms
from .models import Prescricao

class PrescricaoForm(forms.ModelForm):
    
    class Meta:
        model = Prescricao
        exclude = ('medico', 'created_on' , 'updated_on')