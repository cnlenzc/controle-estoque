from rest_framework import serializers
from produto.models import Produto, Categoria, Classificacao
from util import ChoiceDisplayField, PrimaryKeyWihName


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = ('__all__')


class ProdutoSerializer(serializers.ModelSerializer):
    serializer_choice_field = ChoiceDisplayField

    hyperlink = serializers.HyperlinkedRelatedField(source='id', read_only=True, view_name='produto-detail')
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    nome_categoria = serializers.CharField(source='categoria.nome', read_only=True)
    classificacao = serializers.PrimaryKeyRelatedField(queryset=Classificacao.objects.all())
    nome_classificacao = serializers.CharField(source='classificacao.nome', read_only=True)

    class Meta:
        model = Produto
        fields = (
            "id",
            "hyperlink",
            "nome",
            "descricao",
            "categoria",
            "nome_categoria",
            "classificacao",
            "nome_classificacao",
            "situacao",
            "foto_b64",
            "peso",
            "unidade_peso",
            "codigo_barras",
            "codigo_revista",
            "obs",
        )


