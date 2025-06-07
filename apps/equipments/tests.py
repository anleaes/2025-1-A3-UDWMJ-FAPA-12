from django.test import TestCase
from .models import Equipamento

# Create your tests here.

class EquipamentoModelTest(TestCase):
    def test_str(self):
        equipamento = Equipamento(modelo="X1", numero_serie="123456", localizacao="Sala A")
        self.assertEqual(str(equipamento), "X1 - 123456")
