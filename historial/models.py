from django.db import models
from django.contrib import admin
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

class Doctor(models.Model):
    #idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    especialidad  = models.CharField(max_length=30)
    usuario_doctor = models.ForeignKey('auth.User')
    def __str__(self):
        return self.nombre

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre    = models.CharField(max_length=60)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Consulta (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    descripcion_padecimiento = models.CharField(max_length=120)
    fecha_padecimiento = models.DateField()
    tratamiento    = models.CharField(max_length=60)

class ConsultaInLine(admin.TabularInline):
    model = Consulta
    extra = 1

class PacienteAdmin(admin.ModelAdmin):
    inlines = (ConsultaInLine,)

class EnfermedadAdmin (admin.ModelAdmin):
    inlines = (ConsultaInLine,)

class DoctorAdmin (admin.ModelAdmin):
    inlines = (ConsultaInLine,)
