from django.db import models


# Create your models here.
class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=185, unique=True)
    apellido = models.CharField(max_length=185, unique=True)
    telefono = models.IntegerField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=100, null=True)
    
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
    

    codigo = models.CharField(max_length=30, unique=True, verbose_name="Código del curso")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, verbose_name="Programa de Formación")
    instructor_coordinador = models.ForeignKey('instructores.Instructor', on_delete=models.CASCADE, related_name='cursos_coordinados', verbose_name="Instructor Coordinador")
    instructores = models.ManyToManyField('instructores.Instructor', through='InstructorCurso', related_name='cursos_impartidos', verbose_name="Instructores")
    aprendices = models.ManyToManyField(Aprendiz, through='AprendizCurso', related_name='cursos', verbose_name = "Aprendices")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalización")
    horario = models.CharField(max_length=100, verbose_name="Horario")
    aula = models.CharField(max_length=50, verbose_name="Aula/Ambiente")
    cupos_maximos = models.PositiveIntegerField(verbose_name="Cupos Máximos")
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PRO', verbose_name="Estado del Curso")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
