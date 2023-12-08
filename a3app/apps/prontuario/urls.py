from django.urls import path
from . import views

app_name = 'prontuario'

urlpatterns = [
    path('', views.list_prontuario, name='list_prontuario'),
    path('adicionar/', views.add_prontuario, name='add_prontuario'),
    path('editar/<int:id_prontuario>/', views.edit_prontuario, name='edit_prontuario'),
    path('excluir/<int:id_prontuario>/', views.delete_prontuario, name='delete_prontuario'),
]