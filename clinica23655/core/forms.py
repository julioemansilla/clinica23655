from django import forms

class ContactoForms(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    dni = forms.CharField (label='Dni')
    matricula = forms.CharField (label='Matricula')
    email = forms.EmailField(label='Email')