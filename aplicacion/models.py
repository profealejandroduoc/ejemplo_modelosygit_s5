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

    def __str__(self):
        return self.nombre + " " + self.apellido


class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    persona=models.ForeignKey("Persona",on_delete=models.PROTECT)

    def __str__(self):
            return self.nombre