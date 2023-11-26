# urls.py
from django.urls import path
from .views import fazer_pedido

urlpatterns = [
    path('fazer_pedido/', fazer_pedido, name='fazer_pedido'),
    path('sucesso/', lambda request: render(request, 'pedido_sucesso.html'), name='sucesso'),
]
