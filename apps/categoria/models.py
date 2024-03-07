from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=50,blank=True, null=True)
    projetos = models.ManyToManyField('projeto.Projeto',related_name='categorias')
    def __str__(self):
        return str(self.titulo)
