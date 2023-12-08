from django.db import models

# Create your models here.

class Paciente(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    condicao = models.TextField('Condição', max_length=200, default='-')
    idade = models.CharField('Idade', max_length=10)
    CPF = models.IntegerField('CPF', max_length= 11)
    
    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'Pacientes'
        ordering =['id']

    def __str__(self):
        return self.first_name


