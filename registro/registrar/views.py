from django.shortcuts import render, redirect
from .models import Materia
from .models import Alumno
from django.contrib import messages
from .forms import FormularioMateria
from .forms import FormularioAlumno
from .forms import FormularioModificarAlumno, FormularioModificarMateria

def listar(request):
	alumno = Alumno.objects.all()
	materia = Materia.objects.all()
	context={
		'alumno':alumno,
		'materia':materia,
	}
	return render(request,"listar.html",context)


def crearMateria(request):
	f = FormularioMateria(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			m =Materia()
			m.nombre=f_data.get("nombre")
			m.codigo=f_data.get("codigo")
			m.cupos=f_data.get("cupos")
			if(m.save()!=True):
				return redirect(listar)

				
			
	context = {
		'f':f,
	}
	return render(request,"crearmateria.html",context)

def crearAlumno(request):
	f = FormularioAlumno(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			a =Alumno()
			a.nombre=f_data.get("nombre")
			a.apellido=f_data.get("apellido")
			a.cedula=f_data.get("cedula")
			if(a.save()!=True):
				return redirect(listar)

				
			
	context = {
		'f':f,
	}
	return render(request,"crearalumno.html",context)


def ModificarAlumno(request):

	f = FormularioModificarAlumno(request.POST or None)
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context={
		'alumno':alumno,
		'f':f,
	}
	f.fields['nombre'].initial = alumno.nombre
	f.fields['apellido'].initial = alumno.apellido
	
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			alumno.nombre = datos.get("nombre")
			alumno.apellido = datos.get("apellido")
			if (alumno.save()!=True):
				return redirect(listar)

	return render(request,"modificaralumno.html",context)


def ModificarMateria(request):

	f = FormularioModificarMateria(request.POST or None)
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	context={
		'materia':materia,
		'f':f,
	}
	f.fields['nombre'].initial = materia.nombre
	f.fields['cupos'].initial = materia.cupos
	
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			materia.nombre = datos.get("nombre")
			materia.cupos = datos.get("cupos")
			if (materia.save()!=True):
				return redirect(listar)

	return render(request,"modificarmateria.html",context)


def eliminaral(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context = {
		'alumno':alumno,
	}

	return render(request,"eliminaralumno.html",context)

def eliminaralumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el alumno", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el alumno", fail_silently=True)
	return redirect(listar)

def eliminarma(request):
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	context = {
		'materia':materia,
	}

	return render(request,"eliminarmateria.html",context)

def eliminarmateria(request):
	materia = Materia.objects.get(codigo=request.GET['codigo'])
	if materia.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado la materia", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado la materia", fail_silently=True)
	return redirect(listar)