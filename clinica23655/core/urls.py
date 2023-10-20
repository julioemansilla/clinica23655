from django.urls import path
from core.views import * 
from turno.views import nuevo_turno

urlpatterns = [
    path('', Homeview.as_view(), name='index'),
    path('home/<str:nombre_usuario>/', index2, name='nombre_usuario'),
    path('especialidades_listado/', EspecialidadesListView.as_view(), name='especialidades_listado'),
    path('medicos/', DoctorListView.as_view(), name='medicos'),
    path('datos_personales_medico/<str:matricula>', datos_personales_medico, name="datos_personales_medico"),
    path('nuevo_turno/',nuevo_turno, name="nuevo_turno"),
    path('alta', AltaDoctor.as_view(), name = 'alta_medico')
]