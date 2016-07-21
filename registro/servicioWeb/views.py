from registrar.models import Materia
from registrar.models import Alumno
from .serializable import AlumnoSerializable
from .serializable import MateriaSerializable
from rest_framework import viewsets

class AlumnoViewSet(viewsets.ModelViewSet):
	#llamo al objeto serializable
	serializer_class=AlumnoSerializable
	#defino la consulta de datos que se enviaran en la web servise
	queryset=Alumno.objects.all().order_by('apellido')


class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class=MateriaSerializable
	queryset = Materia.objects.exclude(cupos__gte=30)