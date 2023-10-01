from django import forms

class ContactoForms(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    rubro = forms.CharField (label='Rubro')
    matricula = forms.CharField (label='Matricula')
    dni = forms.CharField(label='Dni')
    email = forms.EmailField(label='Email')