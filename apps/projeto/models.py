from django.db import models

class Category(models.TextChoices):
    CARD = 'filter-card'
    APP = 'filter-app'
    WEB = 'filter-web'

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="images/projetos/", blank=True, null=True)
    link_do_github = models.CharField(max_length=254)
    category = models.CharField(max_length=15,choices=Category.choices,default=Category.WEB)
    usuario_id = models.ForeignKey("usuario.CustomUsuarios",default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)
