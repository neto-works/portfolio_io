from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser precisa ter is_superuser como True")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("superuser precisa ter is_staff como True")
        return self._create_user(email, password, **extra_fields)

class CustomUsuarios(AbstractUser):
    email = models.EmailField("E-mail", unique=True, max_length=254)
    fone = models.CharField("Telefone", max_length=15)
    is_staff = models.BooleanField("Membro da equipe", default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "fone"]
    def __str__(self):
        return str(self.email)
    objects = UsuarioManager()
