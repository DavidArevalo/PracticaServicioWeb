from rest_framework import serializers
from registrar.models import Materia
from registrar.models import Alumno

class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model=Alumno
		fields=('cedula','nombre','apellido')

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model=Materia
		fields=('nombre','codigo','cupos')

