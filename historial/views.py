from django.shortcuts import render
from django.shortcuts import redirect
from .models import Doctor

from django.contrib import messages
from .forms import Form_NuevoDoctor,UserForm
from .models import Paciente, Consulta

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse
from django.core import serializers
import pdb #para hacer el debugging
from django.shortcuts import redirect
from .models import *
from django.contrib.auth import login


# Create your views here.
@login_required
def post_list(request):
    doctor_logueado=Doctor.objects.get(usuario_doctor=request.user) #este es el usuario que está logueado en el sistema
    #doctor_logueado=Empleado.objects.get(usuario_doctor=request.user)
    cons = Consulta.objects.filter(doctor=doctor_logueado).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
    #cons = Consulta.objects.filter(doctor=1).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
    #para hacer el filtro por nombre y apellido, sería algo como: objects.filter(doctor__nombre__icontains=variable_nombre,doctor__apellido__icontains=variable_apellido)
    return render(request, 'historial/lista_consultas.html', {'cons': cons})


#def consulta_nueva(request):
#    if request.method == "POST":
#        formulario = ConsultaForm(request.POST)
#        if formulario.is_valid():
#            pelicula = Paciente.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
#            for actor_id in request.POST.getlist('doctores'):
#                actuacion = Consulta(actor_id=actor_id, pelicula_id = pelicula.id)
#                actuacion.save()
#            messages.add_message(request, messages.SUCCESS, 'Consulta Guardada Exitosamente')
#    else:
#        formulario = ConsultaForm()
#    return render(request, 'historial/consulta_editar.html', {'formulario': formulario})

def registro_doctor(request):
    if request.method == 'POST':
        form=Form_NuevoDoctor(request.POST)
        form_usuario=UserForm(request.POST)
        var_error=''
        #sub_form=Form_NuevoDoctor(request.POST, request.FILES)
        if form.is_valid(): #validando a la persona
            if form_usuario.is_valid():
                try:
                    nuevo_doctor=form.save(commit=False)
                    new_user = User.objects.create_user(**form_usuario.cleaned_data)
                    #ultimo_usuario=new_user.save()
                    nuevo_doctor.usuario_doctor=new_user
                    nuevo_doctor.save()
                    form=Form_NuevoDoctor()
                    form_usuario=UserForm()
                except Exception as e:
                    var_error=str(e)
            #mensaje error (raise error)
    else:
        var_error=''
        form=Form_NuevoDoctor()
        form_usuario=UserForm()
    return render(request, 'historial/doctor.html', {'form': form, 'form_usuario':form_usuario,'errores':var_error})
