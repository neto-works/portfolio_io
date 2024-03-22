from django.db import models


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    likes = models.IntegerField()
    imagem = models.ImageField(upload_to="images/posts/", blank=True, null=True)
    blogueiro_id = models.ForeignKey("blogueiro.Blogueiro", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.titulo)
