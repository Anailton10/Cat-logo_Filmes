from django.db import models


class Cadastro_Filmes(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.TextField()
    capa = models.FileField(upload_to='capa')
    duracao = models.IntegerField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
