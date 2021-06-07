from django.contrib import admin

from .models import Produto, Categoria, Fornecedor, Estoque, ProdutoVendido

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Estoque)
admin.site.register(ProdutoVendido)