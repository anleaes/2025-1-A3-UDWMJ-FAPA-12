from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
 # clients(models): parte 1 – criar modelo Client

    def __str__(self):
        return self.nome

