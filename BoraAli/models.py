from django.db import models
from datetime import datetime


# Create your models here.


class Trilha(models.Model):
    nome_trilha = models.CharField(max_length=200)
    descricao = models.TextField()
    localizacao = models.TextField()
    duracao = models.IntegerField()
    nivel = models.CharField(max_length=20)
    curiosidades = models.CharField(max_length=400, blank=True, null=True)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
