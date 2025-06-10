from django.shortcuts import render, get_object_or_404, redirect
from .models import SolicitacaoServico
from .forms import SolicitacaoServicoForm

# Create your views here.

def list_solicitacoes(request):
    solicitacoes = SolicitacaoServico.objects.all()
    return render(request, 'services/list_solicitacoes.html', {'solicitacoes': solicitacoes})

def add_solicitacao(request):
    if request.method == 'POST':
        form = SolicitacaoServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services:list_solicitacoes')
    else:
        form = SolicitacaoServicoForm()
    return render(request, 'services/add_solicitacao.html', {'form': form})
# services(views): parte 1 – adicionar list/add views

def edit_solicitacao(request, id):
    solicitacao = get_object_or_404(SolicitacaoServico, id=id)
    if request.method == 'POST':
        form = SolicitacaoServicoForm(request.POST, instance=solicitacao)
        if form.is_valid():
            form.save()
            return redirect('services:list_solicitacoes')
    else:
        form = SolicitacaoServicoForm(instance=solicitacao)
    return render(request, 'services/add_solicitacao.html', {'form': form})

def delete_solicitacao(request, id):
    solicitacao = get_object_or_404(SolicitacaoServico, id=id)
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('services:list_solicitacoes')
    return render(request, 'services/delete_solicitacao.html', {'solicitacao': solicitacao})