from django.db import models

# Create your models here.

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
# parts(models): parte 1 – criar classe Peca

    def calcular_custo(self, quantidade):
        return self.custo_unitario * quantidade

    def __str__(self):
        return self.nome
# parts(models): parte 2 – método calcularCusto