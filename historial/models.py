from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre    = models.CharField(max_length=60)
    apellido = models.CharField(max_length=50)
    especialidad  = models.CharField(max_length=30)
    Padecimientos   = models.ManyToManyField(Paciente, through='Padecimiento')
    def __str__(self):
        return self.nombre

class Padecimiento (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=120)
    fecha_padecimiento = models.DateField()

class PadecimientoInLine(admin.TabularInline):
    model = Padecimiento
    extra = 1

class PacienteAdmin(admin.ModelAdmin):
    inlines = (PadecimientoInLine,)

class DoctorAdmin (admin.ModelAdmin):
    inlines = (PadecimientoInLine,)
