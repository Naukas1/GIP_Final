from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Especialidades(models.Model):
    """ Informacion de las obras sociales """

    Nombre = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.Nombre

    def get_url_esp_crear(self):
        return reverse('especialidad:crear')

    def get_url_lista(self):
        return reverse('especialidad:contactos')

class Profesionales(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    EMail = models.EmailField()
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

    def get_url_detalle(self):
        return reverse('profesionales:detalle', kwargs={"id":self.id})

    def get_url_lista(self):
        return reverse('profesionales:lista')

    def get_url_edita(self):
        return reverse('profesionales:update', kwargs={"id":self.id})

    def get_url_borrar(self):
        return reverse('profesionales:borrar', kwargs={"id":self.id})

    def get_url_crear(self):
        return reverse('profesionales:crear')


