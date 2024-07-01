from django.db import models
# Create your models here.
class Estudiante(models.Model):
    codigo = models.CharField(max_length=10)
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=100)
    apemat = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=9)
    estado = models.CharField(max_length=1)

