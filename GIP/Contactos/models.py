from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class ObraSocial(models.Model):
    """ Informacion de las obras sociales"""

    Nombre = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Obra Social"
        verbose_name_plural = "Obras Sociales"

    def __str__(self):
        return self.Nombre

    # TODO: Analyze and add fields as needed. I'm guessing legal stuff like Persona Juridica
    # TODO: Create view and add get_absolute_url function

class Contactos(models.Model):
    Nombre = models.CharField(max_length=120)
    Apellido = models.CharField(max_length=64)
    Documento = models.IntegerField()
    Telefono = models.IntegerField()
    EMail = models.EmailField(max_length=120)
    FNacimiento = models.DateField()
    ObraSocial = models.ForeignKey(ObraSocial, on_delete=models.PROTECT, null=True) #This shouldnt let us delete an entry of ObraSocial if a Contacto has it assigned
    NroAfiliado = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.Nombre

    def get_url_detalle(self):
        return reverse('contactos:detalle', kwargs={"id":self.id})

    def get_url_lista(self):
        return reverse('contactos:lista')

    def get_url_edita(self):
        return reverse('contactos:update', kwargs={"id":self.id})

    def get_url_borrar(self):
        return reverse('contactos:borrar', kwargs={"id":self.id})

    def get_url_crear(self):
        return reverse('contactos:crear')





