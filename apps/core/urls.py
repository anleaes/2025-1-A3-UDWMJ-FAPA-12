from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('clientes/', include('clients.urls', namespace='clients')),
    path('equipamentos/', include('equipments.urls', namespace='equipments')),
    path('tecnicos/', include('technicians.urls', namespace='technicians')),
    path('servicos/', include('services.urls', namespace='services')),
    path('pecas/', include('parts.urls', namespace='parts')),
    path('faturas/', include('invoices.urls', namespace='invoices')),
]