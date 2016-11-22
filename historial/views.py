from django.shortcuts import render
from .models import Doctor, Enfermedad

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

from historial.models import Paciente, Padecimiento
from django.utils import timezone
from .models import Paciente, Padecimiento

from .forms import EnfermedadForm, PacienteForm
from django.shortcuts import redirect
from .forms import *
from .models import *
# Create your views here.
@login_required
def post_list(request):
    doctor_logueado=Doctor.objects.get(usuario_doctor=request.user) #este es el usuario que está logueado en el sistema
    cons = Consulta.objects.filter(doctor=doctor_logueado).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
    #para hacer el filtro por nombre y apellido, sería algo como: objects.filter(doctor__nombre__icontains=variable_nombre,doctor__apellido__icontains=variable_apellido)
    return render(request, 'historial/lista_consultas.html', {'cons': cons})


#def post_list(request):
#    doctor_logueado=Doctor.objects.get(usuario_doctor=request.user) #este es el usuario que está logueado en el sistema
#    #doctor_logueado=Empleado.objects.get(usuario_doctor=request.user)
#    cons = Consulta.objects.filter(doctor=doctor_logueado).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
#    #cons = Consulta.objects.filter(doctor=1).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
#    #para hacer el filtro por nombre y apellido, sería algo como: objects.filter(doctor__nombre__icontains=variable_nombre,doctor__apellido__icontains=variable_apellido)
#    return render(request, 'historial/lista_consultas.html', {'cons': cons})


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

#------------Nueva Enfermedad--------------------------------

def nueva_enfermedad(request):
    if request.method == "POST":
        formulario = EnfermedadForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Enfermedad Guardada Exitosamente')
            #return redirect('historial/lista_consultas.html', pk=post.pk)
    else:
        formulario = EnfermedadForm()
    return render(request, 'historial/enfermedad_editar.html', {'formulario': formulario})

#-------Nuevo Paciente---------------------
def nuevo_paciente(request):
    if request.method == "POST":
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            paciente = Paciente.objects.create(nombre=formulario.cleaned_data['nombre'], apellido = formulario.cleaned_data['apellido'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'])
            for enfermedad_id in request.POST.getlist('enfermedades'):
                padecimiento = Padecimiento(enfermedad_id=enfermedad_id, paciente_id = paciente.id)
                padecimiento.save()
                messages.add_message(request, messages.SUCCESS, 'Paciente Guardado Exitosamente')
    else:
        formulario = PacienteForm()
    return render(request, 'historial/ingresar_paciente.html', {'formulario': formulario})

#-----------------Nueva Consulta

def consulta_nueva(request):
    if request.method == "POST":
        form_consulta = Form_Consulta(request.POST)
        if form_consulta.is_valid():
            doctor_logueado=Doctor.objects.get(usuario_doctor=request.user) #este es el usuario que está logueado en el sistema
            consulta = form_consulta.save(commit=False)
            consulta.doctor=doctor_logueado
            messages.add_message(request, messages.SUCCESS, 'Consulta Guardada Exitosamente')
    else:
        doctor_logueado=Doctor.objects.get(usuario_doctor=request.user) #este es el usuario que está logueado en el sistema
        form_consulta = Form_Consulta()
        #Lo siguiente sirve para filtrar lo que se muestra en los combobox, se debe colocar también en el if, porque al recargar la página el filtro se eliminaría, por eso se debe agregar también ahí, para que vuelva a filtrar.
        #form_consulta.fields["paciente"].queryset = Paciente.objects.filter(estado_paciente=1)
    return render(request, 'historial/consulta_editar.html', {'form_consulta': form_consulta})
#----------------------------------------------------------------

#fields = ('nombre', 'apellido', 'fecha_nacimiento','enfermedades')
#paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
#descripcion_padecimiento = models.CharField(max_length=120)
#fecha_padecimiento = models.DateField()
#tratamiento    = models.CharField(max_length=60)
