from django.db import models

class Chamada(models.Model):
    nome = models.CharField(max_length=200, null=False)
    presenca = models.CharField(max_length=10, null=False)