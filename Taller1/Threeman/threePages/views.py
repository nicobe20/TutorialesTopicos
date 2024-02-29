from django.shortcuts import render, redirect
from .models import Cliente
from .forms import *
def home(request):
    return render(request, 'threePages/index.html')

def creado(request):
    return render(request, 'threePages/creado.html')


def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('creado')  
    else:
        form = ClienteForm()
    return render(request, 'threePages/crearCliente.html', {'form': form})

def listarClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'threePages/listarClientes.html', {'clientes': clientes})

def verCliente(request, cliente_id):
    #cliente = Cliente.objects.get(id=cliente_id)
    clientes = Cliente.objects.all()
    return render(request, 'threePages/verCliente.html', {'clientes': clientes})

def borrarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('listarClientes')  