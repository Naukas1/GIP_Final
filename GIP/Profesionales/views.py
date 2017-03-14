from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesionales
from django.contrib.auth.models import User
from .forms import Profesionales_Form, Usuario_Form
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
#
# def contactos_crear(request):
#     form = Contactos_Form(request.POST or None)
#     if form.is_valid():
#         instancia = form.save(commit=False)
#         instancia.save()
#         messages.success(request, "Creado Exitosamente!")
#         return HttpResponseRedirect(instancia.get_absolute_url())
#     context = {
#         "form": form,
#     }
#     return render(request, "contactos_form.html", context)
#
def profesionales_editar(request, id=None):
    #Retrieve our profesional and calls its form
    instancia_prof = get_object_or_404(Profesionales,id=id)
    profesionales_form = Profesionales_Form(request.POST or None, instance=instancia_prof)

    #Retrieve the instance of user associated with our profesional and call its form

    # instancia_usu = get_object_or_404(User,id=instancia_prof.Usuario.id) #This here proves I'm awesome
    # usuario_form = Usuario_Form(request.POST or None, instance=instancia_usu)

    if profesionales_form.is_valid():
        instancia_prof = profesionales_form.save(commit=False)
        instancia_prof.save()

        # instancia_usu = usuario_form.save(commit=False)  #Further proof of my awesomeness
        # instancia_usu.save()

        messages.success(request, "Profesional Actualizado!")

        return HttpResponseRedirect(instancia_prof.get_absolute_url())
    context = {
        "profesionales_form": profesionales_form,
        # "usuario_form": usuario_form,
        "instancia": instancia_prof,
        }

    return render(request, "profesionales_editar_form.html", context)
#
# def contactos_borrar(request,  id=None):
#     instancia = get_object_or_404(Contactos, id=id)
#     instancia.delete()
#     messages.success(request, "Contacto Borrado!")
#
#     return redirect("contactos:lista")

