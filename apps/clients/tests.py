from django.test import TestCase
from .models import Cliente

# Create your tests here.

class ClienteModelTest(TestCase):
    def test_str(self):
        cliente = Cliente(nome="Fulano", email="f@x.com", endereco="Rua 1", telefone="123")
        self.assertEqual(str(cliente), "Fulano")
