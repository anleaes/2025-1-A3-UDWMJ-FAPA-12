from django.contrib import admin
from .models import SolicitacaoServico, Agendamento

# Register your models here.

@admin.register(SolicitacaoServico)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'data_solicitacao')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitacao', 'data', 'periodo_horario')
