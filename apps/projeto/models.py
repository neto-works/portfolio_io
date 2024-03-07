from django.db import models


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    usuario_id = models.ForeignKey('usuario.CustomUsuarios',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.titulo)
