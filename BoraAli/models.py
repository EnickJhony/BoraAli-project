from django.db import models

# Create your models here.
class Trilha(models.model):
    nome_trilha = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    localizacao = 
    duracao = 
    nivel = 
    curiosidades = 