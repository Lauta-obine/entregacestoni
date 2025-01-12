from django import forms


class TractorFormulario (forms.Form):
    patente = forms.CharField(max_length=8)
    marca = forms.CharField(max_length=20)
    ano = forms.IntegerField()

class SemiFormulario (forms.Form):
    patente = forms.CharField(max_length=8)
    marca = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    ano = forms.IntegerField()

class ChoferFormulario (forms.Form):
   
    nombre = forms.CharField(max_length=20)
    dni = forms.IntegerField()  
    

