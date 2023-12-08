from django.db import models
from paciente.models import Paciente

# Create your models here.
class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Agendado', 'Agendado'),
        ('Cancelado', 'Cancelado')
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Agendado')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'atendimento'
        verbose_name_plural = 'atendimentos'
        ordering =['-created_on']

    def __str__(self):
        return  self.status


