from django.urls import path
from django.contrib.auth import views as auth_views 

from core.views import * 


urlpatterns = [
    path('', Homeview.as_view(), name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name= 'login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name= 'logout'),

    path('home/<str:nombre_usuario>/', index2, name='nombre_usuario'),
    path('especialidades/', EspecialidadesListView.as_view(), name='especialidades'),
    path('medicos/', DoctorListView.as_view(), name='medicos'),
    path('datos_personales_medico/<int:pk>', datos_personales_medico, name='datos_personales_medico'),
    path('turnos/',TurnosListView.as_view(), name='turnos'),
    path('pacientes/',PacienteListView.as_view(), name='pacientes'),
    path('buscador/', BlogSearchView.as_view(), name = 'buscador'),
    path('alta_turno/',AltaTurno.as_view(), name='alta_turno'),
    path('alta_medico', AltaDoctor.as_view(), name = 'alta_medico'),
    path('alta_paciente', AltaPaciente.as_view(), name='alta_paciente'),
    path('alta_especialidad', AltaEspecialidad.as_view(), name = 'alta_especialidad'),
]