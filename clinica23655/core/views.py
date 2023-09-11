from django.http import HttpResponse
import datetime
from django.shortcuts import render

"""def index(request):
    return HttpResponse('index.html')"""

def index(request):
    return render ( request, 'index.html' )

def especialidades_listado(request):
    return HttpResponse("""
<ul>
    <li>Clinica General Adultos</li>
    <li>Pediatria</li>
    <li>Cardiologia</li>                    
</ul>
"""
    )
def turnos_dia(request):
    now=datetime.datetime.now()
    return HttpResponse(f'<h1> Turnos del dia: {now}</h1>')