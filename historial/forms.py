from django import forms
from .models import Paciente, Doctor, Consulta


class ConsultaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Consulta
        fields = ('paciente', 'doctor', 'enfermedad',)
#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
def __init__ (self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields["consultas"].queryset = Doctor.objects.all()
        self.fields["consultas"].queryset = Paciente.objects.all()
        self.fields["consultas"].queryset = Enfermedad.objects.all()
        self.fields["consultas  "].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["doctores"].help_text = "Ingrese los Actores que participaron en la película"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
