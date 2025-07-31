from django.db import models


# Create your models here.
class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=185, unique=True)
    apellido = models.CharField(max_length=185, unique=True)
    telefono = models.IntegerField(max_length=10, unique=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    ciudad = models.CharField(max_length=185, null=True)
    programa = models.CharField(max_length=185)


def __str__(self):
    return f"{self.nombre} {self.apellido} - {self.documento_identidad}"
