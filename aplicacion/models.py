from django.db import models

# Create your models here.

SEXO = [
    ("F", "Femenino"),
    ("M", "Masculino"),
    ("O", "Otro"),]

class Persona(models.Model):
    rut=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    f_nacimiento=models.DateField()
    sexo=models.CharField(max_length=1,choices=SEXO)
