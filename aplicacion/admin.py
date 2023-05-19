from django.contrib import admin
from .models import Persona, Mascota
# Register your models here.

class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","f_nacimiento","sexo"]
    list_editable=["nombre","apellido","f_nacimiento","sexo"]

    class meta:
        model=Persona

class admMascota(admin.ModelAdmin):
    list_display=["id","nombre","tipo","persona"]
    list_editable=["nombre","tipo","persona"]


    class meta:
        model=Mascota


admin.site.register(Persona,admPersona)
admin.site.register(Mascota,admMascota)