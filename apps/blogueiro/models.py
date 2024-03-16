from django.db import models


# Create your models here.
class Blogueiro(models.Model):
    hastag = models.CharField(max_length=50, blank=True, null=True)
    quant_post = models.IntegerField()
    usuario_id = models.OneToOneField(
        "usuario.CustomUsuarios", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.hastag)
