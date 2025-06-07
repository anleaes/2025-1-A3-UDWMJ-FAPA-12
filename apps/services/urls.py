from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.list_solicitacoes, name='list_solicitacoes'),
    path('add/', views.add_solicitacao, name='add_solicitacao'),
    path('edit/<int:id>/', views.edit_solicitacao, name='edit_solicitacao'),
    path('delete/<int:id>/', views.delete_solicitacao, name='delete_solicitacao'),
]