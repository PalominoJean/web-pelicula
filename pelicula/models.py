from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    id_usuario=models.IntegerField()
    nombre=models.CharField(max_length=30)
    contrasenia=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Director(models.Model):
    id_director=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Actor(models.Model):
    id_autor=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    id_genero=models.IntegerField()
    nombre=models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    id_pelicula=models.IntegerField()
    titulo=models.CharField(max_length=30)
    fecha_publicacion=models.DateTimeField(default=timezone.now)
    anio_estreno=models.IntegerField()
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    portada=models.ImageField(upload_to='portada')
    directores=models.ManyToManyField(Director)
    actores=models.ManyToManyField(Actor)
    generos=models.ManyToManyField(Genero)
    def __str__(self):
        return self.titulo
