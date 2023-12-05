from django.db import models
from mercado.models import Categoria
from uploader.models import Image

class Fruta(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.IntegerField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="frutas"
    )
    descricao = models.CharField(max_length=255)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome