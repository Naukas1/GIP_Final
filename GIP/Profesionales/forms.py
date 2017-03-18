from django import forms
from .models import Profesionales, Especialidades
from django.contrib.auth.models import User
import datetime

class Usuario_Form(forms.ModelForm):

    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

class Profesionales_Form(forms.ModelForm):

    lista = []
    # Lista vacia a popular con los posibles anos de la fecha de nacimiento
    actual = datetime.datetime.now().year + 1  # Ano actual para definir el final de la lista

    for i in range(1900, actual):
        lista.append(i)

    FNacimiento = forms.DateField(widget=forms.SelectDateWidget(years=lista))

    class Meta:
        model = Profesionales
        fields = [
            "Usuario",
            "Nombre",
            "Apellido",
            "EMail",
            "Matricula",
            "Documento",
            "Telefono",
            "FNacimiento",
            "Especialidad",
        ]

class Especialidades_Form(forms.ModelForm):

    class Meta:
        model = Especialidades
        fields = [
            "Nombre",
        ]
