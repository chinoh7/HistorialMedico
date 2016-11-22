from django import forms
from .models import Paciente, Doctor, Enfermedad, Consulta


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

def post_edit(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        formulario = PostearForm(request.POST, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        formulario = PostearForm(instance=post)
    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})




#---------------------------------------------------
class ConsultaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Consulta
        fields = ('paciente', 'doctor', 'enfermedad','descripcion_padecimiento','fecha_padecimiento','tratamiento')
#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
def __init__ (self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields["consultas"].queryset = Doctor.objects.all()
        self.fields["consultas"].queryset = Paciente.objects.all()
        self.fields["consultas"].queryset = Enfermedad.objects.all()
        self.fields["doctore  "].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["consultas"].help_text = "Ingrese los Actores que participaron en la película"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
#-----------------------------------------------------------------

class Form_Consulta(forms.ModelForm):
    def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
        # first call parent's constructor
        super(Form_Consulta, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['doctor'].required = False

    class Meta:
        model=Consulta
        fields=('paciente','doctor','enfermedad','descripcion_padecimiento','fecha_padecimiento','tratamiento')




#fields = ('nombre', 'apellido', 'fecha_nacimiento','enfermedades')
#paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
#doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
#descripcion_padecimiento = models.CharField(max_length=120)
#fecha_padecimiento = models.DateField()
#tratamiento    = models.CharField(max_length=60)
