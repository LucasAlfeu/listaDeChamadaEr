from django.db import models

class Chamada(models.Model):
    nome = models.CharField(max_length=150, null=False)
    presenca = models.CharField(max_length=150, null=False, name='presenca')

    def __str__(self):
        return self.nome