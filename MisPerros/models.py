from django.db import models
from django.contrib.auth.models import AbstractUser

ct=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
]
options=[
        ('Macho','Macho'),
        ('Hembra','Hembra'),
]
class Perro(models.Model):
    nombre=models.CharField(max_length=20)
    datos=models.TextField(null=True)
    img=models.ImageField(null=True)
    sexo=models.CharField(choices=options, null=True, max_length=6)

    def __str__(self):
        return f"Nombre:{self.nombre},  Datos:{self.datos} {self.img} {self.sexo}"

class Socio(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.CharField(choices=ct, null=True, max_length=1)
    def __str__(self):
        return f"Nombre:{self.nombre},  Categoria:{self.categoria}"

class HogarTemporal(models.Model):
    ubicacion=models.CharField(max_length=40)
    datoshogar=models.CharField(max_length=50)
    def __str__(self):
        return f"Nombre:{self.ubicacion},  Datos:{self.datoshogar}"
    


