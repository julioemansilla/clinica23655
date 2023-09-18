from django.db import models
from django.db import models


from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=200)

class Medico(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class Turno(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario = models.TimeField('Horario del turno')
    fecha = models.DateField('Fecha del turno')

# Create your models here.
