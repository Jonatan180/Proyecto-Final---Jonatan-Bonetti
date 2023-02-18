from django import forms

class PerroFormulario(forms.Form):
    nombre=forms.CharField()
    datos=forms.CharField()

class SocioFormulario(forms.Form):
    nombre=forms.CharField()
    categoria=forms.CharField()

class HogarTemporalFormulario(forms.Form):
    ubicacion=forms.CharField()
    datoshogar=forms.CharField()