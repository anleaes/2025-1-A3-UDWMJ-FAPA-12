from django.test import TestCase
from .models import Fatura

# Create your tests here.
class FaturaModelTest(TestCase):
    def test_adicionar_item(self):
        fatura = Fatura(valor_total=100)
        fatura.adicionar_item("Peça X", 50)
        self.assertEqual(fatura.valor_total, 150)
