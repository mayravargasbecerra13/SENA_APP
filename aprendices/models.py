from django.db import models


# Create your models here.
class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=185, unique=True)
    apellido = models.CharField(max_length=185, unique=True)
    telefono = models.IntegerField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    ciudad = models.CharField(max_length=185, null=True)
    
    class Meta:
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"
        ordering = [ 'apellido', 'nombre']


def __str__(self):
    return f"{self.nombre} {self.apellido} - {self.documento_identidad}"

def nombre_completo(self):
    return f"{self.nombre } {self.apellido}"

class Curso(models.Model):
    ESTADO_CHOICES = [
        ('PRO', 'Programado'),
        ('INI', 'Iniciado'),
        ('EJE', 'En Ejecución'),
        ('FIN', 'Finalizado'),
        ('CAN', 'Cancelado'),
        ('SUS', 'Suspendido'),
    ]
    
    
