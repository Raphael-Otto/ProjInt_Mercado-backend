from django.db import models
from mercado.models import Categoria

class Verdura(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="verduras"
    )

    def __str__(self):
        return self.nome