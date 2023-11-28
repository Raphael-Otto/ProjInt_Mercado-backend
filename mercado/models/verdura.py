from django.db import models
from mercado.models import Categoria
from uploader.models import Image

class Verdura(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.IntegerField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="verduras"
    )
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