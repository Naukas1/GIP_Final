from django import forms
from .models import Contactos
import datetime

class Contactos_Form(forms.ModelForm):

    lista = []
    # Lista vacia a popular con los posibles anos de la fecha de nacimiento
    actual = datetime.datetime.now().year + 1  # Ano actual para definir el final de la lista

    for i in range(1900, actual):
        lista.append(i)

    FNacimiento = forms.DateField(widget=forms.SelectDateWidget(years=lista))
    EMail = forms.EmailField(required=False)

    class Meta:
        model = Contactos
        fields = [
            "Nombre",
            "Apellido",
            "Documento",
            "Telefono",
            "EMail",
            "FNacimiento",
            "ObraSocial",
            "NroAfiliado",
        ]