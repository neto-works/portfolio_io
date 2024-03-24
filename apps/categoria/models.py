from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=50, blank=True, null=True)
    posters = models.ManyToManyField("post.Post", related_name="categorias",blank=True)

    def __str__(self):
        return str(self.titulo)
