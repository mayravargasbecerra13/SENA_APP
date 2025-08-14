from django import forms
from .models import Programa
import datetime

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código", help_text="Código de programa")
    nombre = forms.CharField(max_length=200, label="Nombre del Programa", help_text="Ingrese el Código del Programa")
    nivel_formacion = forms.ChoiceField(choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formación del programa.")
    modalidad = forms.ChoiceField(choices=Programa.MODALIDAD_CHOICES, initial='PRE', label='Modalidad', help_text="Seleccione la modalidad del programa.")
    duracion_meses = forms.IntegerField(label="Duración en Meses", help_text="Ingrese la duración del programa en meses.")
    duracion_horas = forms.IntegerField(label="Duración en Horas", help_text="Ingrese la duración del programa en horas.")
    descripcion = forms.CharField(label="Descripción del Programa", help_text="Ingrese la descripción del programa.")
    competencias = forms.CharField(label="Competencias a Desarrollar", help_text="Ingrese las competencias a desarrollar en el programa.")
    perfil_egreso = forms.CharField(label="Perfil de Egreso", help_text="Ingrese el perfil de egreso del programa.")
    requisitos_ingresos = forms.CharField(label="Requisitos de Ingreso", help_text="Ingrese los requisitos de ingreso del programa.")
    centro_formacion = forms.CharField(label="Centro de Formación", help_text="Ingrese el centro de formación del programa.")
    regional = forms.CharField(label="Regional", help_text="Ingrese el regional del programa.")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, initial='ACT', label="Estado", help_text="Seleccione el estado del programa.")
    fecha_creacion = forms.DateField(label="Fecha de Creación del Programa", help_text="Ingrese la fecha de creación del programa.")
    fecha_registro = forms.DateTimeField(initial=datetime.datetime.now, label="Fecha de Registro", help_text="Ingrese la fecha de registro del programa.")
    
    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('codigo') or not cleaned_data.get('nombre'):
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data
    
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo números.")
        return codigo
    
    def save(self):
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egreso=self.cleaned_data['perfil_egreso'],
                requisitos_ingresos=self.cleaned_data['requisitos_ingresos'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el programa: {str(e)}")