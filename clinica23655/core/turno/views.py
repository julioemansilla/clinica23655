from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello (request):
    return HttpResponse("Hola GENTE!")
def busquedaTurno(request):
    return render(request,"Turnos.html")
from django.shortcuts import render
from .models import Turno

from django.shortcuts import render
from .models import Turno, Medico

def nuevo_turno(request):
    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        medico = Medico.objects.get(id=medico_id)
        horario = request.POST.get('horario')
        fecha = request.POST.get('fecha')
        turno = Turno(medico=medico, horario=horario, fecha=fecha)
        turno.save()
        return render(request, 'turnos/nuevo_turno.html', {'turno': turno})
    else:
        medicos = Medico.objects.all()
        return render(request, 'turnos/nuevo_turno.html', {'medicos': medicos})
