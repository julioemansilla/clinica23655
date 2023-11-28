from django import forms
from django.core.exceptions import ValidationError

from core.models import *

class ContactoForms(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'color_fondo'}),required=True)
    apellido = forms.CharField(label='Apellido',required=True)
    rubro = forms.CharField (label='Rubro',widget=forms.TextInput(attrs={'class':'color_fondo'}),required=True)
    matricula = forms.CharField (label='Matricula',required=True)
    dni = forms.CharField(label='Dni',widget=forms.TextInput(attrs={'class':'color_fondo'}),required=True)
    edad = forms.IntegerField(label='Edad', required=True)
    email = forms.EmailField(label='Email',required=True)

    def clean_edad(self):
        if self.cleaned_data['edad'] < 18:
            raise ValidationError('El doctor/a ingresado no puede tener menos de 18 años')
        
        return self.cleaned_data['edad']


class AltaDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {
            "matricula": forms.TextInput(attrs={"id":"matricula","minlenght":"6","class":"form-control"})
        }

    def clean_edad(self):
        if self.cleaned_data['edad'] < 18:
            raise ValidationError('El doctor/a ingresado no puede tener menos de 18 años')
        
        return self.cleaned_data['edad']
    
    def clean_matricula(self):
        if len(self.cleaned_data['matricula']) < 6:
            raise ValidationError('La matricula debe contener 6 caracteres o más')
        return self.cleaned_data['matricula']
            
class AltaPaciente(forms.ModelForm):
    class Meta: 
        model = Paciente 
        fields = "__all__"

class AltaTurno(forms.ModelForm):
    class Meta: 
        model = Turno
        fields = "__all__"
        widgets = {
            "hora": forms.TimeInput(format="%H:%M", attrs={"type":"time"}),
            "fecha":forms.DateInput(format='%d/%m/%Y', attrs={"type":"date"})
        }

class AltaEspecialidad(forms.ModelForm):
    class Meta:
        model = Especialidad 
        fields = "__all__"