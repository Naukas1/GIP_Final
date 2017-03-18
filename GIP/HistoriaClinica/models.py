from django.db import models
import Contactos
import Profesionales


# Create your models here.
class HistoriaClinica(models.Model):
    """ Cabecera de la historia Clinica """

    Nombre = models.CharField(max_length=64, null=True)
    Paciente = models.ForeignKey(Contactos.models.Contactos, on_delete=models.CASCADE)
    Profesional = models.ForeignKey(Profesionales.models.Profesionales, on_delete=models.PROTECT)

    # TODO: evaluar y agregar campos a esta Historia Clinica generica *Nota: Pediatria va a ser otra app que extienda este modelo, do not add specifics here
    Antecedentes = models.TextField(null=True)
    Alergias = models.TextField(null=True)

    class Meta:
        verbose_name = "Historia Clinica"
        verbose_name_plural = "Historias Clinicas"

    # TODO: Definir una mejor forma de identificar una historia clinica en la lista
    def __str__(self):
        return str(self.Nombre)

    # def get_absolute_url(self):
    #     return reverse('profesionales:detalle', kwargs={"id":self.id})


class HistoriaClinicaDetalle(models.Model):
    """ Lineas de la historia Clinica, a llenarse con cada subsecuente consulta """

    FechaConsulta = models.DateField(auto_now_add=True)
    HistoriaClinica = models.ForeignKey(HistoriaClinica,
                                        on_delete=models.CASCADE)  # Si se borra la HistoriaClinica padre, deberian borrarse todos sus entries en detalle
    Descripcion = models.TextField(null=True)
    Tratamiento = models.TextField(null=True)

    class Meta:
        verbose_name = "Linea de Historia Clinica"
        verbose_name_plural = "Lineas de Historia Clinica"

    def __str__(self):
        return str(self.Tratamiento)
