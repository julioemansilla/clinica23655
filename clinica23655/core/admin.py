from django.contrib import admin
from core.models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'matricula')
    ordering = ('id',)
    list_editable = ('nombre' , 'apellido')
    list_display_links = ['matricula']
    search_fields = ['apellido', 'nombre']

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'dni')
    ordering = ('id',)
    list_editable = ('nombre' , 'apellido')
    list_display_links = ['dni']
    search_fields = ['apellido', 'nombre','dni']

class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id','doctor', 'Paciente', 'hora','fecha')
    ordering = ('id',)
    
    

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Especialidad)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Turno, TurnoAdmin)