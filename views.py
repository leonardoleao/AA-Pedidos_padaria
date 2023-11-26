from django.shortcuts import render, redirect
from .forms import PedidoForm

def fazer_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = PedidoForm()

    return render(request, 'fazer_pedido.html', {'form': form})