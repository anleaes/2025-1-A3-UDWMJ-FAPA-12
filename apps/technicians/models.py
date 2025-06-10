from django.db import models

# Create your models here.

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    especializacao = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
# technicians(models): parte 1 – criar modelo Tecnico

    def __str__(self):
        return self.nome
# technicians(models): parte 2 – métodos adicionais

