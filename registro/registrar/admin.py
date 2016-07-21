from django.contrib import admin
from .models import Alumno
from .models import Materia


class AdministrarAlumno(admin.ModelAdmin):
	list_display = ["__str__","nombre","apellido","cedula"]
	class Meta:
		model = Alumno #agregar un modelo llamado contacto
admin.site.register(Alumno,AdministrarAlumno)

class AdministrarMateria(admin.ModelAdmin):
	list_display = ["__str__","nombre","codigo","cupos"]
	class Meta:
		model = Materia
admin.site.register(Materia,AdministrarMateria)

