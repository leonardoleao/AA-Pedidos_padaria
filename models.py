from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    quantidade = models.PositiveIntegerField()
    nome_cliente = models.CharField(max_length=50)
    endereco_entrega = models.TextField()
    data_pedido = models.DateTimeField(auto_now_add=True)