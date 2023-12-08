from django.urls import path
from . import views

app_name = 'atendimento'

urlpatterns = [
    path('', views.list_atendimento, name='list_atendimento'),
    path('adicionar/<int:id_paciente>/', views.add_atendimento, name='add_atendimento'),
    path('excluir/<int:id_atendimento>/', views.delete_atendimento, name='delete_atendimento'),

    ]