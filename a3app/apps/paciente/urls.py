from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.list_paciente, name='list_paciente'),
    path('adicionar/', views.add_paciente, name='add_paciente'),
    path('editar/<int:id_paciente>/', views.edit_paciente, name='edit_paciente'),
    path('excluir/<int:id_paciente>/', views.delete_paciente, name='delete_paciente'),
    path('buscar/', views.search_paciente, name='search_paciente'),
]