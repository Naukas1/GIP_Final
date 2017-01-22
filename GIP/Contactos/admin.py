from django.contrib import admin

# Register your models here.
from Contactos.models import Contactos, ObraSocial

class ContactosAdmin(admin.ModelAdmin):
    list_display = ["__str__", "Documento"]
    list_filter = ["Documento", "EMail"]
    search_fields = ["Nombre","Apellido"]
    class Meta:
        model = Contactos


admin.site.register(Contactos, ContactosAdmin)
admin.site.register(ObraSocial)