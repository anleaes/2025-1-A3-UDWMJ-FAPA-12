from django.urls import path
from . import views

app_name = 'parts'
# parts(urls): parte 1 – namespace

urlpatterns = [
    path('', views.list_pecas, name='list_pecas'),
    path('add/', views.add_peca, name='add_peca'),
    path('edit/<int:id>/', views.edit_peca, name='edit_peca'),
    path('delete/<int:id>/', views.delete_peca, name='delete_peca'),
]