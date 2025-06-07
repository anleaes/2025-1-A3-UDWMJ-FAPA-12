from django.db import models
from decimal import Decimal

# Create your models here.

class Fatura(models.Model):
    data_emissao = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def adicionar_item(self, descricao, custo):
        self.valor_total += Decimal(custo)

    def __str__(self):
        return f"Fatura #{self.id} - R$ {self.valor_total}"
