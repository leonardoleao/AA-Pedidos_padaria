from django.db import models

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    pedido = models.TextField()
    horario_retirada = models.DateTimeField()

    def __str__(self):
        return f'{self.nome_cliente} - {self.pedido}'
