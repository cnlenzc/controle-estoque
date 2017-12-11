from django.http import HttpResponse
from rest_framework import generics, viewsets
from produto.models import Produto, Categoria, Classificacao
from produto.serializers import ProdutoSerializer, CategoriaSerializer, ClassificacaoSerializer


def index(request):
    return HttpResponse("Olá! Bem vindo ao GenialVendas!")


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ClassificacaoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
