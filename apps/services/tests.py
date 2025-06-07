from django.test import TestCase
from .models import SolicitacaoServico, StatusSolicitacao

# Create your tests here.

class SolicitacaoModelTest(TestCase):
    def test_default_status(self):
        self.assertEqual(StatusSolicitacao.PENDENTE, 'PENDENTE')
