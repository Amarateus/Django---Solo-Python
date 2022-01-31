from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):        # Para que el Post se muestre con el title que le pusimos
        return self.title
        