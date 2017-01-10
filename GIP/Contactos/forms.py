from django import forms
from .models import Contactos

class Contactos_Form(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = [
            "Nombre",
            "Apellido",
            "Documento",
            "Telefono",
            "FNacimiento",

        ]