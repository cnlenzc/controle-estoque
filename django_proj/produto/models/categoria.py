from django.db import models


class Categoria(models.Model):
    nome =\
        models.CharField(help_text='Nome da categoria',
            max_length=30, unique=True, db_index=True)

    situacao =\
        models.CharField(help_text='Situaçao (ativo ou descontinuado)',
            max_length=1, choices=(('1', 'Ativo'), ('2', 'Descontinuado')), default='1')


    def __str__(self):
        return self.nome

