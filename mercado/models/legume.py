from django.db import models
from mercado.models import Categoria

class Legume(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.IntegerField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="legumes"
    )

    def __str__(self):
        return self.nome
    