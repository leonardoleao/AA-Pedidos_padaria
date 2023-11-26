from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['produtos', 'quantidade', 'nome_cliente', 'endereco_entrega']