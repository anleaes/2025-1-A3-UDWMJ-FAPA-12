from django.shortcuts import render, get_object_or_404, redirect
from .models import Tecnico
from .forms import TecnicoForm

# Create your views here.
def list_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'technicians/list_tecnicos.html', {'tecnicos': tecnicos})

def add_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('technicians:list_tecnicos')
    else:
        form = TecnicoForm()
    return render(request, 'technicians/add_tecnico.html', {'form': form})
# technicians(views): parte 1 – adicionar list/add views

def edit_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('technicians:list_tecnicos')
    else:
        form = TecnicoForm(instance=tecnico)
    return render(request, 'technicians/add_tecnico.html', {'form': form})

def delete_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == 'POST':
        tecnico.delete()
        return redirect('technicians:list_tecnicos')
    return render(request, 'technicians/delete_tecnico.html', {'tecnico': tecnico})