from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=40)
    ingredientes = models.CharField(max_length=200)
    preparacion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=40)
    autor = models.CharField(max_length=30)
    fecha = models.DateField(max_length=30)
    imagen = models.CharField(max_length=30)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Administrador(models.Model):
    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
