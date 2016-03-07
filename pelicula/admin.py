from django.contrib import admin
from pelicula.models import Pelicula,Director,Actor,Usuario,Genero
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Usuario)
admin.site.register(Genero)