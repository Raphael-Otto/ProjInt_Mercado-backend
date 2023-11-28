from django.db import models
from mercado.models import Marca, Categoria
from uploader.models import Image

class Carne(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ManyToManyField(Marca, related_name="carnes")
    categoria = models.ManyToManyField(Categoria, related_name="carnes")
    quantidade = models.CharField(max_length=255)
    preco = models.IntegerField(max_length=255)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nome} ({self.marca})"
