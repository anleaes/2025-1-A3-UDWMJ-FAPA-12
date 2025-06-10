from django.db import models
from clients.models import Cliente
from equipments.models import Equipamento
from technicians.models import Tecnico

# Create your models here.

class StatusSolicitacao(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    ATRIBUIDA = 'ATRIBUIDA', 'Atribuída'
    EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em andamento'
    CONCLUIDA = 'CONCLUIDA', 'Concluída'
    CANCELADA = 'CANCELADA', 'Cancelada'

class SolicitacaoServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, blank=True)
    data_solicitacao = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=StatusSolicitacao.choices, default=StatusSolicitacao.PENDENTE)
# services(models): parte 1 – criar SolicitacaoServico

    def __str__(self):
        return f"Solicitação {self.id} - {self.status}"

class Agendamento(models.Model):
    solicitacao = models.OneToOneField(SolicitacaoServico, on_delete=models.CASCADE)
    data = models.DateField()
    periodo_horario = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.solicitacao} - {self.data}"
