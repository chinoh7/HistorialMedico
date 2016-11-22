from django.conf.urls import include, url
from . import views
#from historial.views import RegistroUsuario

urlpatterns = [
        url(r'^listado/$', views.post_list, name='post_list'),
        #url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
        #url(r'^consulta/nueva/$', views.consulta_nueva, name='consulta_nueva'),
        #url(r'^$','django.contrib.auth.views.login',{'template_name':'historial/login.html'}, name='login'),
        url(r'^$','django.contrib.auth.views.login',{'template_name':'historial/index.html'}, name='inicio'),
        url(r'^login/$','django.contrib.auth.views.login',{'template_name':'historial/login.html'}, name='login'),
        url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
        url(r'^nuevodoctor/$',views.registro_doctor,name='nuevo_doctor'),
        url(r'^nuevaenfermedad/$', views.nueva_enfermedad, name='EnfermedadN'),
        url(r'^nuevopaciente/$', views.nuevo_paciente, name='PacienteN'),
        url(r'^nuevaconsulta/$', views.consulta_nueva, name='ConsultaN'),
        url(r'^listapacientes/$', views.lista_pacientes, name='PacienteL'),
        #url(r'^nuevoconsulta/$', views.nuevo_paciente, name='ConsultaN'),

    ]
