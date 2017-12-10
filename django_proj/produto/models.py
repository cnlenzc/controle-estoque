from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

enum_unidade_validade = (('Anos', 'Anos'), ('Meses', 'Meses'), ('Dias', 'Dias'))
enum_unidade_peso = (('gramas', 'gramas'), ('Kg', 'Kg'))

class Produto(models.Model):
    nome = models.CharField(max_length=30, unique=True, db_index=True)
    descricao = models.TextField()
    foto_b64 = models.CharField(max_length=200000, blank=True)
    validade = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    unidade_validade = models.CharField(max_length=10, choices=enum_unidade_validade, default=enum_unidade_validade[0][0])
    peso = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    unidade_peso = models.CharField(max_length=10, choices=enum_unidade_peso, default=enum_unidade_peso[0][0])
    codigo_barras = models.CharField(max_length=100, blank=True)
    codigo_revista = models.CharField(max_length=20, blank=True)
    obs = models.TextField(max_length=1000, blank=True)