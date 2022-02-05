from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):   # Formulario para crear un Post
    class Meta:
        model = Post   # Aca definimos el modelo que vamos a usar. En este caso importamos Post del archivo models.py
        fields = ('title', 'content')   # Los campos que hayamos definido en el model Post