from django.db import models

# Create your models here.
class Prescricao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    medico = models.CharField('Medico', max_length=50)
    description = models.TextField('Descricao', max_length=100, default='-')
    medicamento = models.TextField('Medicamentos', max_length=100, default='-')
    
    class Meta:
        verbose_name = 'Prescricao'
        verbose_name_plural = 'Prescricoes'
        ordering =['id']

    def __str__(self):
        return self.medicamento
        
    