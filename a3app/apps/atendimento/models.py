from django.db import models
from paciente.models import Paciente
from medico.models import Medico
from consulta.models import Consulta


# Create your models here.
class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Agendado', 'Agendado'),
        ('Cancelado', 'Cancelado')
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Agendado')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'atendimento'
        verbose_name_plural = 'atendimentos'
        ordering =['id']

    def __str__(self):
        return  self.status


