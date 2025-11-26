from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    usuario = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    contenido = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def total_comentarios(self):
        return self.comentarios.count()

    def __str__(self):
        return f'{self.usuario.username} - {self.contenido[:20]}'
    

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE)
    contenido = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username}'
    


