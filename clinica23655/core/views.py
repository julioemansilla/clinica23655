from django.http import HttpResponse
import datetime
from django.contrib import messages
from django.shortcuts import render , redirect
from django.urls    import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Doctor, Especialidad, Paciente, Turno
from .forms import ContactoForms, AltaDoctor, AltaTurno, AltaPaciente, AltaEspecialidad

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# def index(request):
#     return render ( request,  )


def alta_medico(request):
    if request.method  == 'POST':
        formulario = ContactoForms(request.POST)

        if formulario.is_valid():
            messages.info(request,'Registro de Medico/a con exito')
            return redirect(reverse('index'))
    else:
        
        formulario = ContactoForms()

    context = {
        'contacto_form': formulario 
    }
    
    return render(request, 'core/alta_medico.html', context)

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
    medicos = [
        {
            'matricula':55486,
            'nombre':'Daniel',
            'apellido':'Espinosa',
            'rubro':'Medico clinico'
        },
        {
            'matricula':89875,
            'nombre':'Isabel',
            'apellido':'Mendez',
            'rubro':'Pediatra'
        },
        {
            'matricula':87926,
            'nombre':'Esteban',
            'apellido':'Rosales',
            'rubro':'Cardiologo'    
        }
    ]
    contexto = {
        'medicos':medicos
    }

    return render(request, 'core/medicos.html',context=contexto)


def datos_personales_medico(request,matricula):
    medicos = [
        {
            'matricula':55486,
            'nombre':'Daniel',
            'apellido':'Espinosa',
            'rubro':'Medico clinico',
            'descripcion': '¡Hola! Soy Daniel Espinosa, un médico clínico apasionado por la salud y el bienestar de mis pacientes. Con años de experiencia en el campo de la medicina, me enorgullece ofrecer atención médica de alta calidad con un enfoque en el trato humano y personalizado. Mi misión es ayudar a las personas a mantener y mejorar su salud, brindando diagnósticos precisos, tratamientos efectivos y asesoramiento comprensivo. Fuera del consultorio, disfruto aprendiendo sobre los avances médicos y manteniéndome al día con las últimas investigaciones para ofrecer a mis pacientes el mejor cuidado posible. Siempre estoy aquí para servir y ayudar a las personas a vivir vidas más saludables y felices.',
            'experiencia':"""Mi experiencia médica abarca varios años de práctica en el campo de la medicina clínica. He trabajado en diversas instituciones médicas, donde he adquirido un amplio conocimiento y habilidades en el diagnóstico, tratamiento y cuidado de pacientes de todas las edades y con una variedad de condiciones médicas. 
            
            Durante mi carrera, he tenido la oportunidad de colaborar con equipos multidisciplinarios, lo que me ha permitido ofrecer un enfoque integral en la atención médica. Además, he seguido formándome y actualizándome constantemente para estar al tanto de los últimos avances en medicina y tecnología médica, lo que me permite brindar a mis pacientes los mejores tratamientos disponibles. 
            
            Mi compromiso principal es proporcionar atención médica de calidad, centrada en el paciente y basada en la evidencia, con un enfoque en el bienestar general y la prevención de enfermedades. Cada día, me siento honrado de poder contribuir a mejorar la salud y la calidad de vida de las personas que confían en mi experiencia médica."""
        },
        {
            'matricula':89875,
            'nombre':'Isabel',
            'apellido':'Mendez',
            'rubro':'Pediatra',
            'descripcion':"""¡Hola! Soy Isabel Méndez, una pediatra dedicada y apasionada por la salud de los niños. Con una sólida formación médica y años de experiencia en el campo pediátrico, me enorgullece ofrecer atención médica especializada y compasiva a los más jóvenes de nuestra comunidad.

            Mi objetivo principal es asegurarme de que cada niño que entra en mi consultorio reciba la atención individualizada que merece. Desde los recién nacidos hasta los adolescentes, me esfuerzo por proporcionar un ambiente cálido y acogedor donde los padres y los niños se sientan cómodos y confiados en mi cuidado.

            Además de mi práctica clínica, también estoy comprometida con la educación y la prevención. Creo firmemente en la importancia de informar a los padres sobre la salud de sus hijos y brindar orientación sobre hábitos saludables desde una edad temprana.

            Es un honor para mí ser parte del crecimiento y desarrollo de los niños, y me esfuerzo por mantenerme actualizada con las últimas investigaciones y avances en medicina pediátrica para brindar el mejor cuidado posible a mis pequeños pacientes. Estoy aquí para apoyar a las familias en su viaje hacia una vida saludable y feliz para sus hijos.""",
            'experiencia':"""Mi experiencia médica abarca varios años de dedicación a la pediatría. Durante este tiempo, he tenido el privilegio de trabajar con niños de todas las edades, desde recién nacidos hasta adolescentes. Mi enfoque siempre ha sido proporcionar una atención médica integral y personalizada que tenga en cuenta las necesidades específicas de cada niño y su familia.

            He trabajado en diversas instituciones médicas y he sido testigo de una amplia variedad de condiciones pediátricas. Esta experiencia me ha permitido desarrollar habilidades sólidas en el diagnóstico y tratamiento de enfermedades infantiles, así como en la promoción de la salud y la prevención de enfermedades.

            Mi pasión por la pediatría se refleja en mi compromiso continuo con la educación médica y la actualización constante. Estoy decidida a mantenerme al día con las últimas investigaciones y avances en el campo de la pediatría para brindar el más alto nivel de atención a mis pacientes y sus familias.

            Cada día, me siento agradecida por la oportunidad de marcar una diferencia en la vida de los niños y contribuir al bienestar de las nuevas generaciones."""
        },
        {
            'matricula':87926,
            'nombre':'Esteban',
            'apellido':'Rosales',
            'rubro':'Cardiologo',
            'descripcion':"""¡Hola! Soy Esteban Rosales, un apasionado cardiólogo comprometido con la salud cardiovascular de mis pacientes. Mi dedicación a este campo de la medicina se basa en mi firme creencia en la importancia de cuidar y proteger el motor vital de nuestro cuerpo: el corazón.

            Mi objetivo es proporcionar una atención cardíaca de la más alta calidad, centrada en el paciente y basada en la evidencia. Cada día, me esfuerzo por establecer relaciones de confianza con mis pacientes y sus familias, brindándoles información y apoyo para tomar decisiones informadas sobre su salud cardiovascular.

            Como cardiólogo, mi enfoque va más allá del diagnóstico y el tratamiento de las enfermedades del corazón; también abogo por la prevención. Creo firmemente en educar a las personas sobre la importancia de un estilo de vida saludable y la gestión de factores de riesgo para reducir las enfermedades cardíacas.""",
            'experiencia':"""Mi experiencia médica en cardiología abarca un período significativo de práctica en diversas instituciones médicas. Durante estos años, he tenido la oportunidad de diagnosticar y tratar una amplia gama de condiciones cardíacas, desde las más comunes hasta las más complejas.

            He trabajado en estrecha colaboración con equipos multidisciplinarios para brindar una atención integral a mis pacientes, incluyendo pruebas de diagnóstico avanzadas, intervenciones médicas y quirúrgicas, y terapia de rehabilitación cardíaca.

            Mi compromiso con la formación continua me ha mantenido actualizado con los últimos avances en cardiología, lo que me permite ofrecer a mis pacientes las opciones de tratamiento más avanzadas y efectivas disponibles.

            Es un privilegio para mí desempeñar un papel en la promoción de la salud cardiovascular y en la mejora de la calidad de vida de mis pacientes. Estoy aquí para ayudar a cada individuo a vivir una vida más larga y saludable a través de un corazón fuerte y saludable."""
        }
    ]
    medico_encontrado = None
    for medico in medicos:
        if medico['matricula'] == matricula:
            medico_encontrado = medico
            break
    return render(request,'core/datos_personales_medico.html',{'medico':medico_encontrado})


class Homeview(TemplateView):
    template_name = 'core/index.html'


class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = 'medicos'
    template_name = 'core/medicos.html'



class AltaDoctor(CreateView):
    model = Doctor
    template_name = 'core/alta_medico.html'
    form_class = AltaDoctor

class EspecialidadesListView(ListView):
    model = Especialidad
    context_object_name = 'especialidades'
    template_name = 'core/especialidades.html'
    
class TurnosListView(LoginRequiredMixin, ListView):
    model = Turno
    context_object_name = 'turnos'
    template_name = 'core/turnos.html'

class AltaTurno(CreateView):
    model = Turno
    template_name = 'core/alta_turno.html'
    form_class = AltaTurno
    

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'core/pacientes.html'

class AltaPaciente(CreateView):
    model = Paciente
    template_name = 'core/alta_paciente.html'
    form_class = AltaPaciente

class AltaEspecialidad(CreateView):
    model = Especialidad
    template_name = 'core/alta_especialidad.html'
    form_class = AltaEspecialidad