from django.urls import path, include
from rest_framework import routers

from .views import ProdutoViewSet, CategoriaViewSet, FornecedorViewSet, EstoqueViewSet, ProdutoVendidoViewSet, StringView

router = routers.SimpleRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'vendidos', ProdutoVendidoViewSet)


urlpatterns = [
  path('', include(router.urls)),
  path('firstchar', StringView.as_view(), name="string"),
]
