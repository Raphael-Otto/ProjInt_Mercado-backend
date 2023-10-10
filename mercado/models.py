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
    marca = models.ManyToManyField(Marca, related_name="carnes")
    categoria = models.ManyToManyField(Categoria, related_name="carnes")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"

class Laticínio(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ManyToManyField(Marca, related_name="laticínios")
    categoria = models.ManyToManyField(Categoria, related_name="laticínios")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"

class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.ManyToManyField(Marca, related_name="bebidas")
    categoria = models.ManyToManyField(Categoria, related_name="bebidas")
    quantidade = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} ({self.marca})"
    
class Fruta(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="frutas"
    )

    def __str__(self):
        return self.nome
    
class Legume(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="legumes"
    )

    def __str__(self):
        return self.nome
    
class Verdura(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="verduras"
    )

    def __str__(self):
        return self.nome