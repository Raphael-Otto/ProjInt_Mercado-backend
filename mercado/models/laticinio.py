from django.db import models
from mercado.models import Marca, Categoria

class Laticínio(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ManyToManyField(Marca, related_name="laticínios")
    categoria = models.ManyToManyField(Categoria, related_name="laticínios")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"
