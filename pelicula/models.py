from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    contrasenia=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    roles=models.ManyToManyField(Rol)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre+" "+self.apellido

class Genero(models.Model):
    nombre=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo=models.CharField(max_length=30)
    fecha_publicacion=models.DateTimeField(default=timezone.now)
    anio_estreno=models.IntegerField()
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    portada=models.ImageField(upload_to='portada')
    personas=models.ManyToManyField(Persona)
    generos=models.ManyToManyField(Genero)
    def __str__(self):
        return self.titulo
