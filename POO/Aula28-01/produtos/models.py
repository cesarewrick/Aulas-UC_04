from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField()
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE, related_name="produtos")

    def __str__(self):
        return f"{self.nome} - {self.fornecedor.nome}"



# Create your models here.
