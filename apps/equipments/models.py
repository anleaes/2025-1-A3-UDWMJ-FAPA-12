from django.db import models

# Create your models here.

class Equipamento(models.Model):
    numero_serie = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.modelo} - {self.numero_serie}"
