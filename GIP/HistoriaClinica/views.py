from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Contactos, Profesionales, HistoriaClinica, HistoriaClinicaDetalle
from .forms import HistoriaClinica_Form, HistoriaClinicaDetalle_Form
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def historiaclinica_detalle(request, id):
    queryset = HistoriaClinicaDetalle.objects.all
    instancia = get_object_or_404(HistoriaClinica, id=id)
    instancia_lineas = get_list_or_404(HistoriaClinicaDetalle, HistoriaClinica__pk=id)

    form = HistoriaClinicaDetalle_Form(request.POST or None)

    if form.is_valid():
        saves = form.save(commit=False)
        saves.save()
        messages.success(request, "Creado Exitosamente!")
        #return HttpResponseRedirect(instancia.get_url_lista())
        return  HttpResponseRedirect("/historiaclinica/")

    context = {
        "instancia": instancia,
        "nombre": instancia.Nombre,
        "lineas": instancia_lineas,
        "object_list": queryset,
        "form": form,
    }

    return render(request, "historiaclinica_detalle.html", context)

def historiaclinica_crear(request):
    #instancia = get_object_or_404(HistoriaClinica)
    form = HistoriaClinica_Form(request.POST or None)
    if form.is_valid():
        saves = form.save(commit=False)
        saves.save()
        messages.success(request, "Creado Exitosamente!")
        #return HttpResponseRedirect(instancia.get_url_lista())
        return  HttpResponseRedirect("/historiaclinica/")
    context = {
        "form": form,
    }
    return render(request, "historiaclinica_form.html", context)

def historiaclinica_lista(request): #trae todos los contactos y los muestra
    queryset = HistoriaClinica.objects.all
    if request.user.is_authenticated():
        context = {
	        "title": "Lista de HCs",
	        "object_list": queryset,
	    }
    else:
        context = {
	    "title": "Lista / No logueado"
	}
    return render(request, "historiaclinica_lista.html", context)

def historiaclinica_borrar(request,  id=None):
    instancia = get_object_or_404(HistoriaClinica, id=id)
    instancia.delete()
    messages.success(request, "Historia Clinica Borrada!")

    return redirect("historiaclinica:lista")

def historiaclinica_update(request, id):
    instancia = get_object_or_404(HistoriaClinica,id=id)
    form = HistoriaClinica_Form(request.POST or None, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
        messages.success(request, "Historia Clinica Actualizada!")

        return HttpResponseRedirect(instancia.get_url_lista())
    context = {
        "form": form,
        "instancia": instancia,
        }

    return render(request, "historiaclinica_update_form.html", context)