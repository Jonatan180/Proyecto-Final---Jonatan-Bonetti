from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MisPerros.models import Perro

class PerroFormulario(ModelForm):
    class Meta:
        model=Perro
        fields=['nombre','datos','img','sexo']

class SocioFormulario(forms.Form):
    nombre=forms.CharField()
    categoria=forms.CharField()

class HogarTemporalFormulario(forms.Form):
    ubicacion=forms.CharField()
    datoshogar=forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='email',widget=forms.EmailInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='email',widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password1', 'password2','email']


