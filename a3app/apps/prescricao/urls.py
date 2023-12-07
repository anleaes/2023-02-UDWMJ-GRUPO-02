from django.urls import path
from . import views

app_name = 'prescricao'

urlpatterns = [
    path('', views.list_prescricao, name='list_prescricao'),
    path('adicionar/<int:id_prescricao>/', views.add_prescricao, name='add_prescricao'),
    path('excluir/<int:id_prescricao>/', views.delete_prescricao, name='delete_prescricao'),
    path('excluir-item/<int:id_prescricao_item>/', views.delete_prescricao_item, name='delete_prescricao_item'),
    path('adicionar-item/<int:id_prescricao>/', views.add_prescricao_item, name='add_prescricao_item'),
    path('editar-status/<int:id_prescricao>/', views.edit_prescricao_status, name='edit_prescricao_status'),
]
