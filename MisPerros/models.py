from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre=models.CharField(max_length=20)
    datos=models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class HogarTemporal(models.Model):
    ubicacion=models.CharField(max_length=40)
    datoshogar=models.CharField(max_length=50)
    def __str__(self):
        return self.ubicacion