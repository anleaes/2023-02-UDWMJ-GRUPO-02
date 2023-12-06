from django.urls import path
from . import views

app_name = 'medico'

urlpatterns = [
    path('', views.list_medicos, name='list_medico'),
    path('adicionar/', views.add_medico, name='add_medico'),
    path('editar/<int:id_medico>/', views.edit_medicos, name='edit_medico'),
    path('excluir/<int:id_medico>/', views.delete_medico, name='delete_medico'),
]