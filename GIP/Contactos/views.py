from django.shortcuts import render, get_object_or_404, redirect
from .models import Contactos
from .forms import Contactos_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
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
    return render(request, "contactos_lista.html", context)


def contactos_detalle(request, id):
    instancia = get_object_or_404(Contactos, id=id)
    context = {
        "instancia": instancia,
        "nombre": instancia.Nombre,
    }
    return render(request, "detalle.html", context)

def contactos_crear(request):
    form = Contactos_Form(request.POST or None)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Creado Exitosamente!")
        return HttpResponseRedirect(instancia.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "contactos_form.html", context)

def contactos_update(request, id=None):
    instancia = get_object_or_404(Contactos,id=id)
    form = Contactos_Form(request.POST or None, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Contacto Actualizado!")

        return HttpResponseRedirect(instancia.get_absolute_url())
    context = {
        "form": form,
        "instancia": instancia,
        }

    return render(request, "contactos_form.html", context)

def contactos_borrar(request,  id=None):
    instancia = get_object_or_404(Contactos, id=id)
    instancia.delete()
    messages.success(request, "Contacto Borrado!")

    return redirect("contactos:lista")