from django.db import models

# Create your models here.

class Consulta(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    address = models.CharField('Endereco', max_length=200)
    cell_phone = models.CharField('Telefone', max_length=20)
    TURNO_CHOICES = (
        ('M', 'Manha'),
        ('T', 'Tarde'),
    )
    turno = models.CharField('Turno', max_length=1, choices=TURNO_CHOICES)
    hora = models.CharField('Hora', max_length=6)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['id']
    
    def __str__(self):
        return self.name


