from django.shortcuts import render
from django.urls    import reverse_lazy

from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

from core.models import Doctor, Especialidad, Paciente, Turno
from .forms import ContactoForms, AltaDoctor, AltaTurno, AltaPaciente, AltaEspecialidad

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


def index2(request,nombre_usuario):
    context ={
        'nombre_usuario':nombre_usuario,
    }
    return render ( request, 'core/index.html',context )


class Homeview(TemplateView):
    template_name = 'core/index.html'


class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = 'medicos'
    template_name = 'core/medicos.html'
    



class AltaDoctor(PermissionRequiredMixin,CreateView):
    model = Doctor
    template_name = 'core/alta_medico.html'
    form_class = AltaDoctor
    permission_required = 'core.add_doctor'
    

class EspecialidadesListView(ListView):
    model = Especialidad
    context_object_name = 'especialidades'
    template_name = 'core/especialidades.html'
    
    
class TurnosListView(LoginRequiredMixin, ListView):
    model = Turno
    context_object_name = 'turnos'
    template_name = 'core/turnos.html'
    
class BlogSearchView(ListView):
    model = Turno
    template_name = 'core/turnos.html'
    context_object_name = 'turnos'
    # FILTRA LA CONSULTA DEL PARAMETRO NOMBRE 
    def get_queryset(self):
        nombre = self.request.GET.get('buscador')
        object_list = Turno.objects.filter(doctor__nombre__icontains = nombre) 
        if object_list:
            return object_list
        else:
            object_list = Turno.objects.filter(Paciente__nombre__icontains = nombre) 
            return object_list

class AltaTurno(PermissionRequiredMixin,CreateView):
    model = Turno
    template_name = 'core/alta_turno.html'
    form_class = AltaTurno
    success_url = reverse_lazy('turnos')
    permission_required = 'core.add_turno'


class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'core/pacientes.html'
    

class AltaPaciente(PermissionRequiredMixin,CreateView):
    model = Paciente
    template_name = 'core/alta_paciente.html'
    form_class = AltaPaciente
    permission_required = 'core.add_paciente'
    

class AltaEspecialidad(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Especialidad
    template_name = 'core/alta_especialidad.html'
    form_class = AltaEspecialidad
    permission_required = 'core.add_especialidad'

    
def datos_personales_medico(request,pk):
    medico = Doctor.objects.filter(id=pk)

    return render(request,'core/datos_personales_medico.html',{'medico':medico})
