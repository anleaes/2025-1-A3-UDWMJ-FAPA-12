"""
URL configuration for manutencaoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('equipamentos/', include('equipments.urls', namespace='equipments')),
    path('tecnicos/', include('technicians.urls', namespace='technicians')),
    path('servicos/', include('services.urls', namespace='services')),
    path('pecas/', include('parts.urls', namespace='parts')),
    path('faturas/', include('invoices.urls', namespace='invoices')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
