from django.shortcuts import render
from django.shortcuts import redirect
from .models import Doctor

from django.contrib import messages
from .forms import ConsultaForm
from .models import Paciente, Consulta

# Create your views here.
def post_list(request):
    #doctor_logueado=Doctor.objects.get(usuario_doctor='1') #este es el usuario que está logueado en el sistema
    #doctor_logueado=
    cons = Consulta.objects.filter(doctor=1).values('doctor__nombre','doctor__apellido','paciente__nombre','paciente__apellido','enfermedad__nombre','descripcion_padecimiento','fecha_padecimiento','tratamiento','pk').order_by('pk')
    #para hacer el filtro por nombre y apellido, sería algo como: objects.filter(doctor__nombre__icontains=variable_nombre,doctor__apellido__icontains=variable_apellido)
    return render(request, 'historial/post_list.html', {'cons': cons})


def consulta_nueva(request):
    if request.method == "POST":
        formulario = ConsultaForm(request.POST)
        if formulario.is_valid():
            pelicula = Paciente.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('doctores'):
                actuacion = Consulta(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Consulta Guardada Exitosamente')
    else:
        formulario = ConsultaForm()
    return render(request, 'historial/consulta_editar.html', {'formulario': formulario})
