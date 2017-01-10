from django.shortcuts import render, get_object_or_404
from .models import Contactos
from django.http import HttpResponse
# Create your views here.

def contactos_lista(request): #trae todos los contactos y los muestra
    queryset = Contactos.objects.all
    if request.user.is_authenticated():
        context = {
            "title": "Mi lista de usuarios",
            "object_list": queryset,
        }
    else:
        context = {
        "title": "Lista / No logueado"
    }
    return render(request, "index.html", context)


def contactos_detalle(request):
    instancia = get_object_or_404(Contactos, id=2)
    context = {
        "instancia": instancia,
        "nombre": instancia.Nombre,
    }
    return render(request, "detalle.html", context)


def contactos_crear(request):
    context = {
        "title": "Crear"
    }

    return render(request, "index.html", context)


def contactos_update(request):
    context = {
        "title": "Update"
    }

    return render(request, "index.html", context)

def contactos_borrar(request):
    context = {
        "title": "Borrar"
    }

    return render(request, "index.html", context)