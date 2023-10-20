from django.contrib import admin

from core.models import *

admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(Turno)