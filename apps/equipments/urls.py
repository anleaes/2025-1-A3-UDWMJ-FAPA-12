from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    path('', views.list_equipamentos, name='list_equipamentos'),
    path('add/', views.add_equipamento, name='add_equipamento'),
    path('edit/<int:id>/', views.edit_equipamento, name='edit_equipamento'),
    path('delete/<int:id>/', views.delete_equipamento, name='delete_equipamento'),
]