from django.contrib import admin
from pelicula.models import Pelicula,Persona,Usuario,Genero,Rol
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Rol)