from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm

# Create your views here.
def list_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipments/list_equipamentos.html', {'equipamentos': equipamentos})

def add_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipments:list_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'equipments/add_equipamento.html', {'form': form})
# equipments(views): parte 1 – adicionar list e add views

def edit_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipments:list_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipments/add_equipamento.html', {'form': form})

def delete_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipments:list_equipamentos')
    return render(request, 'equipments/delete_equipamento.html', {'equipamento': equipamento})