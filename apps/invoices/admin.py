from django.contrib import admin
from .models import Fatura

# Register your models here.

@admin.register(Fatura)
class FaturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_emissao', 'valor_total')


