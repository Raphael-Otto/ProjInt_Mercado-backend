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
    marca = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"