from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .categoria import Categoria
from .classificacao import Classificacao


class Produto(models.Model):
    nome =\
        models.CharField(help_text='Nome do produto',
            max_length=30, unique=True, db_index=True)

    descricao =\
        models.TextField(help_text='Descrição do produto')

    categoria =\
        models.ForeignKey(Categoria, help_text='Categoria conforme a linha',
            default=None, related_name='produtos', on_delete=models.PROTECT)

    classificacao =\
        models.ForeignKey(Classificacao, help_text='Classificação conforme o tipo de uso',
            default=None, related_name='produtos', on_delete=models.PROTECT)

    situacao =\
        models.CharField(help_text='Situaçao (ativo ou descontinuado)',
            max_length=1, choices=(('1', 'Ativo'), ('2', 'Descontinuado')), default='1')

    foto_b64 =\
        models.CharField(help_text='Foto transformada em base64',
            max_length=200000, blank=True)

    peso =\
        models.PositiveIntegerField(help_text='Peso em gramas ou Kg',
            default=0, validators=[MinValueValidator(0), MaxValueValidator(9999)])

    unidade_peso =\
        models.CharField(help_text='Unidade de peso utilizada (gramas ou Kg)',
            max_length=1, choices=(('1', 'gramas'), ('2', 'Kg')), default='1')

    codigo_barras =\
        models.CharField(help_text='Código de barras',
            max_length=100, blank=True)

    codigo_revista =\
        models.CharField(help_text='Código da revista',
            max_length=20, blank=True)

    obs =\
        models.TextField(help_text='Observação',
            blank=True)


    def __str__(self):
        return self.nome