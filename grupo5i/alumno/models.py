from django.db import models

# Create your models here.

class Alumnos(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre")
    fecha_nacimiento=models.DateField(verbose_name="fecha de nacimiento", null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name="fecha de ingreso", null=False,blank=False)