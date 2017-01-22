from django.contrib import admin

# Register your models here.
from Profesionales.models import Profesionales, Especialidades

#TODO: add the User fields in the Profesionales admin view (check model relationship)
admin.site.register(Profesionales)
admin.site.register(Especialidades)