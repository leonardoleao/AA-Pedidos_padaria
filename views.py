from django.shortcuts import render, redirect
from .forms import PedidoForm
from .models import Pedido

def pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = PedidoForm()

    pedidos = Pedido.objects.all()
    return render(request, 'padaria/pedidos.html', {'form': form, 'pedidos': pedidos})
