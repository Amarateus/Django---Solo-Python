from django.db import models

# Los modelos nos permiten editar las informacion de manera dinamica: leer, borrar, actualizar, crear
# Los models son la informacion que se envia a la base de datos
# Las migraciones son los cambios que hacemos en el archivo de models.py

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):        # Para que el Post se muestre con el title que le pusimos.
        return self.title     # self hace referencia a Post


