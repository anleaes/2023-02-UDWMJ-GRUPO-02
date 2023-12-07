from django.db import models
from medico.models import Medico

# Create your models here.
class Prescricao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    # STATUS_CHOICES = (
    #     ('Em andamento', 'Em andamento'),
    #     ('Finalizado', 'Finalizado'),
    #     ('Cancelado', 'Cancelado'),
    # )
    
    #status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Prescrição'
        verbose_name_plural = 'Prescrições'
        ordering =['-created_on']
        
    