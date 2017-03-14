from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Especialidades(models.Model):
    """ Informacion de las obras sociales"""

    Nombre = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.Nombre

class Profesionales(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=64, null=True)
    Apellido = models.CharField(max_length=64, null=True)
    Email = models.EmailField(null=True)
    Documento = models.IntegerField()
    Telefono = models.IntegerField()
    FNacimiento = models.DateField()
    Especialidad = models.ForeignKey(Especialidades, on_delete=models.PROTECT, null=True) #This shouldnt let us delete an entry of ObraSocial if a Contacto has it assigned
    Matricula = models.IntegerField()

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return str(self.Nombre)

    def get_absolute_url(self):
        return reverse('profesionales:detalle', kwargs={"id":self.id})