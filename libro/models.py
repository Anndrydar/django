from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from categoria.models import Catego

# Create your models here.

class Projecto(models.Model):
    grupo = models.ForeignKey(Catego, on_delete = models.CASCADE)
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=1000)
    image = ImageField(upload_to="porta/img/", null = True)
    url = URLField(blank=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.url)


