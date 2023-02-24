from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.fields import CharField
from libro.models import Projecto
# Create your models here.

class Comentario(models.Model):
    libro = models.ForeignKey(Projecto, on_delete = models.CASCADE)
    lector = CharField(max_length=50)
    descripcion = CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        texto2 = "{0} ({1})"
        return texto2.format(self.lector, self.descripcion)


