from django.db import models
from django.contrib.auth.models import User


class Persona2(User):
    class Metal:
        proxy = True 

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    contacto = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Especialidad(models.Model):
    nombre = models.CharField(max_length=70,null=True)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
    
    def get_absolute_url(self):
        return 'especialidades'

class Doctor(Persona):
    matricula = models.CharField(max_length=50,unique=True)
    especialidades = models.ManyToManyField(Especialidad)

    def get_absolute_url(self):
        return 'medicos'
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Paciente(Persona):
    historia_clinica = models.TextField()

    def get_absolute_url(self):
        return 'pacientes'
    
    def __str__(self):
        return  f'{self.nombre}, {self.apellido}'


class Turno(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        return 'turnos'
    
    def __str__(self):
        return f'Doctor: {self.doctor} - Paciente: {self.Paciente}-- Fecha y Hora del Turno: {self.fecha} - {self.hora}'