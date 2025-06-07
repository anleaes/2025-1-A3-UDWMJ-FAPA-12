from django.contrib import admin
from .models import Equipamento
# Register your models here.
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'numero_serie')


