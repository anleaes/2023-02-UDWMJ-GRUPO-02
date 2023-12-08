from django.db import models
from paciente.models import Paciente
from exame.models import Exame
from prescricao.models import Prescricao

# Create your models here.

class Prontuario(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    photo = models.ImageField('Foto', upload_to='photos')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, null=True)
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.photo