from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

# Listar
def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clients/list_clientes.html', {'clientes': clientes})

# Adicionar
def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clients/add_cliente.html', {'form': form})

# Editar
def edit_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clients:list_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clients/add_cliente.html', {'form': form})

# Deletar
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clients:list_clientes')
    return render(request, 'clients/delete_cliente.html', {'cliente': cliente})