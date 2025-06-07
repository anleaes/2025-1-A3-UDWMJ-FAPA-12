from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.list_clientes, name='list_clientes'),
    path('add/', views.add_cliente, name='add_cliente'),
    path('edit/<int:id>/', views.edit_cliente, name='edit_cliente'),
    path('delete/<int:id>/', views.delete_cliente, name='delete_cliente'),
]