from django.urls import path
from . import views

app_name = 'invoices'
# invoices(urls): parte 1 – namespace

urlpatterns = [
    path('', views.list_faturas, name='list_faturas'),
    path('add/', views.add_fatura, name='add_fatura'),
    path('edit/<int:id>/', views.edit_fatura, name='edit_fatura'),
    path('delete/<int:id>/', views.delete_fatura, name='delete_fatura'),
]
# invoices(urls): parte 2 – rotas iniciais