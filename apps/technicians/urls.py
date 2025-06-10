from django.urls import path
from . import views

app_name = 'technicians'
# technicians(urls): parte 1 – namespace

urlpatterns = [
    path('', views.list_tecnicos, name='list_tecnicos'),
    path('add/', views.add_tecnico, name='add_tecnico'),
    path('edit/<int:id>/', views.edit_tecnico, name='edit_tecnico'),
    path('delete/<int:id>/', views.delete_tecnico, name='delete_tecnico'),
]
# technicians(urls): parte 2 – rotas básicas