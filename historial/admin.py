from django.contrib import admin
from historial.models import Paciente, PacienteAdmin, Doctor, DoctorAdmin, Enfermedad, EnfermedadAdmin


admin.site.register(Enfermedad, EnfermedadAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
