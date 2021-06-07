from rest_framework import serializers

from .models import Categoria, Produto, Fornecedor, Estoque, ProdutoVendido

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    depth = 1
    fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Produto
    depth = 1
    fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fornecedor
    depth = 1
    fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Estoque
    depth = 2
    fields = '__all__'

class ProdutoVendidoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProdutoVendido
    depth = 1
    fields = '__all__'