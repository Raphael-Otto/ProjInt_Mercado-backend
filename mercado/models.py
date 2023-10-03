from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Carne(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="carnes")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="carnes"
    )

    def __str__(self):
        return f"{self.nome} ({self.marca})"

class Laticínio(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="laticínios")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="laticínios"
    )

    def __str__(self):
        return f"{self.nome} ({self.marca})"