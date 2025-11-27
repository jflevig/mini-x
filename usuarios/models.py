from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
