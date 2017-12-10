from django.http import HttpResponse
from rest_framework import generics, viewsets
from produto.models import Produto
from produto.serializers import ProdutoSerializer


def index(request):
    return HttpResponse("Olá! Bem vindo ao GenialVendas!")


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
