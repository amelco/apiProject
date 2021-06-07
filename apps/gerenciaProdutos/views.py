from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Produto, Categoria, Fornecedor, Estoque, ProdutoVendido
from .mySerializers import ProdutoSerializer, CategoriaSerializer, FornecedorSerializer, EstoqueSerializer, ProdutoVendidoSerializer

class StringView(APIView):
  def get(self, request, format=None):
    if 'string' in request.GET:
      string = request.GET["string"]
    else:
      return Response("", status=200)

    from libs.string import FirstChar
    obj = FirstChar()
    vogal = obj.compute(string)

    result = {
      "string": string,
      "vogal": vogal,
      "tempoTotal": f"{obj.tempoTotal}ms",
    }
    return Response(result, status=200)

class ProdutoViewSet(viewsets.ModelViewSet):
  serializer_class = ProdutoSerializer
  queryset = Produto.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
  serializer_class = CategoriaSerializer
  queryset = Categoria.objects.all()

class FornecedorViewSet(viewsets.ModelViewSet):
  serializer_class = FornecedorSerializer
  queryset = Fornecedor.objects.all()

class EstoqueViewSet(viewsets.ModelViewSet):
  serializer_class = EstoqueSerializer
  queryset = Estoque.objects.all()

  @action(detail=False)
  def prodFaltosos(self, request):
    qs = self.get_queryset().filter(quantidade = 0)
    serializer = self.get_serializer(qs, many=True)
    res = set()
    print(serializer.data)
    for prod in serializer.data:
      res.add(prod['produto_id']['nome'])
    return Response(res)

  @action(detail=False)
  def fornFaltosos(self, request):
    qs = self.get_queryset().filter(quantidade = 0)
    serializer = self.get_serializer(qs, many=True)
    res = set()
    for prod in serializer.data:
      res.add(prod['produto_id']['fornecedor_id']['nome'])
    return Response(res)
  
  @action(detail=False)
  def quantCategoria(self, request):
    qs = self.get_queryset().filter(quantidade__gt=0)
    serializer = self.get_serializer(qs, many=True)
    res = []
    currCategorie = serializer.data[0]['produto_id']['categoria_id']['nome']
    soma = 0
    for prod in serializer.data:
      if prod['produto_id']['categoria_id']['nome'] == currCategorie:
        soma += prod['quantidade']
      else:
        res.append({'categoria': currCategorie, 'quantidadeEmEstoque': soma})
        soma = prod['quantidade']
      currCategorie = prod['produto_id']['categoria_id']['nome']

    res.append({'categoria': currCategorie, 'quantidadeEmEstoque': soma})
    return Response(res)


class ProdutoVendidoViewSet(viewsets.ModelViewSet):
  serializer_class = ProdutoVendidoSerializer
  queryset = ProdutoVendido.objects.all()

# Criar viewsets de:
# - Categorias e Estoque
# - Produtos == 0 no estoque
# - Fornecedores e Estoque == 0
