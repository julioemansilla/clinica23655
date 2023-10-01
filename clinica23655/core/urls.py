from django.urls import path
from core.views import * 
from turno.views import nuevo_turno

urlpatterns = [
    path('home/', index, name='index'),
    path('home/<str:nombre_usuario>/', index2, name='nombre_usuario'),
    path('especialidades_listado/', especialidades_listado, name='especialidades_listado'),
    path('medicos/', medicos, name='medicos'),
    path('datos_personales_medico/<int:matricula>', datos_personales_medico, name="datos_personales_medico"),
    path('nuevo_turno/',nuevo_turno, name="nuevo_turno"),
    path('contacto', contacto, name = 'contacto')
]