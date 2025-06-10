from django.shortcuts import render, get_object_or_404, redirect
from .models import Fatura
from .forms import FaturaForm

# Create your views here.

def list_faturas(request):
    faturas = Fatura.objects.all()
    return render(request, 'invoices/list_faturas.html', {'faturas': faturas})

def add_fatura(request):
    if request.method == 'POST':
        form = FaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices:list_faturas')
    else:
        form = FaturaForm()
    return render(request, 'invoices/add_fatura.html', {'form': form})
# invoices(views): parte 1 – adicionar list/add views


def edit_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    if request.method == 'POST':
        form = FaturaForm(request.POST, instance=fatura)
        if form.is_valid():
            form.save()
            return redirect('invoices:list_faturas')
    else:
        form = FaturaForm(instance=fatura)
    return render(request, 'invoices/add_fatura.html', {'form': form})

def delete_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    if request.method == 'POST':
        fatura.delete()
        return redirect('invoices:list_faturas')
    return render(request, 'invoices/delete_fatura.html', {'fatura': fatura})
# invoices(views): parte 2 – refinar edição
