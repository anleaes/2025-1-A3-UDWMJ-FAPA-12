from django.test import TestCase
from .models import Tecnico

# Create your tests here.
class TecnicoModelTest(TestCase):
    def test_str(self):
        tecnico = Tecnico(nome="Carlos", especializacao="Elétrica", telefone="11999999999")
        self.assertEqual(str(tecnico), "Carlos")
