from django.db import models

class Alumno(models.Model):
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	cedula = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.cedula

class Materia(models.Model):
	nombre = models.CharField(max_length=60)
	codigo = models.CharField(max_length=10,unique=True)
	cupos = models.IntegerField(default=0)
	def __str__(self):
		return self.codigo