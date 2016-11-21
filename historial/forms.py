from django import forms
from .models import Paciente, Doctor, Enfermedad


class Form_NuevoDoctor(forms.ModelForm):
    def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
        # first call parent's constructor
        super(Form_NuevoDoctor, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['usuario_doctor'].required = False
    class Meta:
        model=Doctor
        fields=('nombre','apellido','direccion','especialidad','usuario_doctor',)
        #widgets = {
        #    'fecha_contratacion_empleado': forms.DateInput(attrs={'class': 'datepicker'}),
        #}

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

#----------------------------------------
class EnfermedadForm(forms.ModelForm):

    class Meta:
        model = Enfermedad
        fields = ('nombre',)
#---------------------------------------
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'fecha_nacimiento','enfermedades')

def __init__ (self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.fields["enfermedades"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["enfermedades"].help_text = "Ingrese las Enfermedades que padece:"
        self.fields["enfermedades"].queryset = Enfermedad.objects.all()

#fields = ('nombre', 'apellido', 'fecha_nacimiento','enfermedades')
#paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
#descripcion_padecimiento = models.CharField(max_length=120)
#fecha_padecimiento = models.DateField()
#tratamiento    = models.CharField(max_length=60)
