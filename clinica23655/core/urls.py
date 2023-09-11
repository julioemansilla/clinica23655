from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('especialidades_listado/', views.especialidades_listado, name='especialidades_listado'),
    path('turnos_dia/', views.turnos_dia, name='turnos_dia')
]