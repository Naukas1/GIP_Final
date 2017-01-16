from django import forms
from .models import Contactos

class Contactos_Form(forms.ModelForm):
    FNacimiento = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Contactos
        fields = [
            "Nombre",
            "Apellido",
            "Documento",
            "Telefono",
            "EMail",
            "FNacimiento",
        ]