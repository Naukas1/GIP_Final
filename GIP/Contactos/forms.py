from django import forms
from .models import Contactos

class Contactos_Form(forms.ModelForm):
    FNacimiento = forms.DateField(input_formats=['%d-%m-%Y']),
    class Meta:
        model = Contactos
        fields = [
            "Nombre",
            "Apellido",
            "Documento",
            "Telefono",
            "FNacimiento",
        ]