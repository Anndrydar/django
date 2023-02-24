from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.fields import CharField

# Create your models here.

class Catego(models.Model):
    nombre = CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        texto3 = "{0} ({1})"
        return texto3.format(self.nombre, self.date)


