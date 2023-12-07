from django import forms
from .models import Exame

class ExameForm(forms.ModelForm):

    class Meta:
        model = Exame
        exclude = ('created_on' , 'updated_on',)