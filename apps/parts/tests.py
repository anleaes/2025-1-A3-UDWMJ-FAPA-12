from django.test import TestCase
from .models import Peca
from decimal import Decimal

# Create your tests here.

class PecaModelTest(TestCase):
    def test_calcular_custo(self):
        peca = Peca(nome="Motor", custo_unitario=Decimal('100.00'))
        self.assertEqual(peca.calcular_custo(3), Decimal('300.00'))
