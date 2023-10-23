from django.urls import path
from core.views import * 
from turno.views import nuevo_turno

urlpatterns = [
    path('', Homeview.as_view(), name='index'),
    path('home/<str:nombre_usuario>/', index2, name='nombre_usuario'),
    path('especialidades/', EspecialidadesListView.as_view(), name='especialidades'),
    path('medicos/', DoctorListView.as_view(), name='medicos'),
    path('datos_personales_medico/<str:matricula>', datos_personales_medico, name='datos_personales_medico'),
    path('turnos/',TurnosListView.as_view(), name='turnos'),
    path('pacientes/',PacienteListView.as_view(), name='pacientes'),
    
    path('alta_turno/',AltaTurno.as_view(), name='alta_turno'),
    path('alta_medico', AltaDoctor.as_view(), name = 'alta_medico'),
    path('alta_paciente', AltaPaciente.as_view(), name='alta_paciente'),
    path('alta_especialidad', AltaEspecialidad.as_view(), name = 'alta_especialidad'),
]