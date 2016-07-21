from django import forms
from .models import Alumno
from .models import Materia

class FormularioAlumno(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["nombre","apellido","cedula"]


class FormularioMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","codigo","cupos"]

class FormularioModificarMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupos"]

class FormularioModificarAlumno(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["nombre","apellido"]