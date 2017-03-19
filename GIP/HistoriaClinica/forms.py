from django import forms
from .models import HistoriaClinica, HistoriaClinicaDetalle
import datetime

class HistoriaClinica_Form(forms.ModelForm):

    class Meta:
        model = HistoriaClinica
        fields = [
            "Nombre",
            "Paciente",
            "Profesional",
            "Antecedentes",
            "Alergias",
            "Diagnostico",

        ]


class HistoriaClinicaDetalle_Form(forms.ModelForm):
    class Meta:
        model = HistoriaClinicaDetalle
        fields = [
            "Descripcion",
            "Tratamiento",

        ]