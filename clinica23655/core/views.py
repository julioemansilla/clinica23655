from django.http import HttpResponse
import datetime
from django.shortcuts import render



def index(request):
    return render ( request, 'core/index.html' )

def index2(request,nombre_usuario):
    context ={
        'nombre_usuario':nombre_usuario,
    }
    return render ( request, 'core/index.html',context )

def especialidades_listado(request):
    return render (request, 'core/especialidades.html')

def turnos_dia(request):
    now=datetime.datetime.now()
    return HttpResponse(f'''
                        {{% block main %}}
                        <h1> Turnos del dia: {now}</h1>
                        {{% endblock %}}''')



def medicos(request):
    return render (request, 'core/medicos.html')