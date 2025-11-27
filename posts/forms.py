from django import forms
from .models import Post, Comentario


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['contenido']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        