from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Contactos(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    Documento = models.IntegerField()
    Telefono = models.IntegerField()
    EMail = models.EmailField(max_length=120)
    FNacimiento = models.DateField()

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('contactos:detalle', kwargs={"id":self.id})
