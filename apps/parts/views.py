from django.shortcuts import render, get_object_or_404, redirect
from .models import Peca
from .forms import PecaForm

# Create your views here.

def list_pecas(request):
    pecas = Peca.objects.all()
    return render(request, 'parts/list_pecas.html', {'pecas': pecas})

def add_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parts:list_pecas')
    else:
        form = PecaForm()
    return render(request, 'parts/add_peca.html', {'form': form})

def edit_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('parts:list_pecas')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'parts/add_peca.html', {'form': form})

def delete_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    if request.method == 'POST':
        peca.delete()
        return redirect('parts:list_pecas')
    return render(request, 'parts/delete_peca.html', {'peca': peca})
