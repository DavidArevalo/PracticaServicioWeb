from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^crearmateria/$', 'registrar.views.crearMateria'),
    url(r'^crearalumno/$', 'registrar.views.crearAlumno'),
    url(r'^modificaralumno/$', 'registrar.views.ModificarAlumno'),
    url(r'^modificarmateria/$', 'registrar.views.ModificarMateria'),
    url(r'^eliminaralumno/$', 'registrar.views.eliminaralumno'),
    url(r'^eliminaral/$', 'registrar.views.eliminaral'),
    url(r'^eliminarmateria/$', 'registrar.views.eliminarmateria'),
    url(r'^eliminarma/$', 'registrar.views.eliminarma'),
    url(r'^$', 'registrar.views.listar'),
    
]


