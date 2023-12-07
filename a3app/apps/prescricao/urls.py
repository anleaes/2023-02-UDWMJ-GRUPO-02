from django.urls import path
from . import views

app_name = 'prescricao'

urlpatterns = [
    path('', views.list_prescricao, name='list_prescricao'),
    path('adicionar/', views.add_prescricao, name='add_prescricao'),
    path('editar/<int:id_prescricao>/', views.edit_prescricao, name='edit_prescricao'),
    path('excluir/<int:id_prescricao>/', views.delete_prescricao, name='delete_prescricao'),
]
