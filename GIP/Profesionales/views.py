from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesionales, Especialidades
from django.contrib.auth.models import User
from .forms import Profesionales_Form, Usuario_Form, Especialidades_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def profesionales_lista(request):
    queryset = Profesionales.objects.all
    if request.user.is_authenticated():
        context = {
            "title": "Mi lista de profesionales",
            "object_list": queryset,
        }
    else:
        context = {
        "title": "Lista / No logueado"
    }
    return render(request, "profesionales_lista.html", context)


def profesionales_detalle(request, id):
    instancia = get_object_or_404(Profesionales, id=id)
    context = {
        "instancia": instancia,
        "nombre": instancia.Nombre,
    }
    return render(request, "profesionales_detalle.html", context)

def profesionales_crear(request):
    form = Profesionales_Form(request.POST or None)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Creado Exitosamente!")
        return HttpResponseRedirect(instancia.get_url_lista())
    context = {
        "form": form,
    }
    return render(request, "profesionales_form.html", context)


def profesionales_edita(request, id):
    instancia = get_object_or_404(Profesionales,id=id)
    form = Profesionales_Form(request.POST or None, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Profesional Actualizado!")

        return HttpResponseRedirect(instancia.get_url_lista())
    context = {
        "form": form,
        "instancia": instancia,
        }

    return render(request, "profesionales_editar_form.html", context)


def profesionales_borrar(request,  id=None):
    instancia = get_object_or_404(Profesionales, id=id)
    instancia.delete()
    messages.success(request, "Profesional Borrado!")

    return redirect("profesionales:lista")


def especialidad_crear(request):
    form = Especialidades_Form(request.POST or None)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Creado Exitosamente!")
        return HttpResponseRedirect("/profesionales")
    context = {
        "form": form,
    }
    return render(request, "especialidades_form.html", context)
