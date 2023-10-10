from django.db import models
from mercado.models import Marca, Categoria

class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ManyToManyField(Marca, related_name="bebidas")
    categoria = models.ManyToManyField(Categoria, related_name="bebidas")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"
