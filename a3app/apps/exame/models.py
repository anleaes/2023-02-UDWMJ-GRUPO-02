from django.db import models

# Create your models here.
class Exame(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    descricao = models.TextField('Descrição', max_length=200, default='')
 
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
        ordering =['id']

    def __str__(self):
        return self.descricao