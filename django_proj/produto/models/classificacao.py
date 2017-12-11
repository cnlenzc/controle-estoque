from django.db import models


class Classificacao(models.Model):
    nome =\
        models.CharField(help_text='Nome da classificação',
            max_length=30, unique=True, db_index=True)


    def __str__(self):
        return self.nome
