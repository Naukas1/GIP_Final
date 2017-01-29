from django.contrib import admin

# Register your models here.
from .models import HistoriaClinica, HistoriaClinicaDetalle

admin.site.register(HistoriaClinica)
admin.site.register(HistoriaClinicaDetalle)
