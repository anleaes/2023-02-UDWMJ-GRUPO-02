from django.urls import path
from . import views

app_name = 'exame'

urlpatterns = [
    path('', views.list_exame, name='list_exame'),
    path('adicionar/', views.add_exame, name='add_exame'),
    path('editar/<int:id_exame>/', views.edit_exame, name='edit_exame'),
    path('excluir/<int:id_exame>/', views.delete_exame, name='delete_exame'),
]