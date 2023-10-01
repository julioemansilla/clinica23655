from django import forms
from django.core.exceptions import ValidationError

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