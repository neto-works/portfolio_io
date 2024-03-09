from django.db import models

# Create your models here.
class Contato(models.Model):
    cidade = models.CharField( max_length=254)
    email = models.EmailField(max_length=254)
    telefone = models.CharField( max_length=50)
    descricao  = models.TextField()
    
    def __str__(self):
        return str(self.email)