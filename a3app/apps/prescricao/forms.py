from django import forms
from .models import Prescricao

class PrescricaoForm(forms.ModelForm):

    class Meta:
        model = Prescricao
        exclude = ('created_on' , 'updated_on',)