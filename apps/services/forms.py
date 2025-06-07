from django import forms
from services.models import SolicitacaoServico, Agendamento  

class SolicitacaoServicoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoServico
        fields = '__all__'

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'