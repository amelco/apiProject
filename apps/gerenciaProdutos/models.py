from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Fornecedor(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Produto(models.Model):
  nome = models.CharField(max_length=100)
  valor_compra = models.FloatField()
  valor_venda = models.FloatField()
  quantidade = models.IntegerField()
  categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  fornecedor_id = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.nome} em {self.fornecedor_id.nome} ({self.quantidade})"
  
class Estoque(models.Model):
  produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.IntegerField()

  def __str__(self):
    return self.produto_id.nome

class ProdutoVendido(models.Model):
  produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
  quantidade = models.IntegerField()

  def __str__(self):
    return self.produto_id.nome
