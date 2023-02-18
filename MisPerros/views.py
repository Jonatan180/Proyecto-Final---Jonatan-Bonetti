from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MisPerros.models import Perro, HogarTemporal, Socio
from MisPerros.forms import HogarTemporalFormulario, PerroFormulario, SocioFormulario
# Create your views here.
def inicio(request):
    return render(request,"MisPerros/inicio.html")
def perro(request):
    return render(request,"MisPerros/perro.html")
def socio(request):
    return render(request,"MisPerros/socio.html")
def hogartemporal(request):
    return render(request,"MisPerros/hogartemporal.html")

def PerroForm(request):
    if request.method == "POST":
        myform=PerroFormulario(request.POST)
        print(myform)

        if myform.is_valid:
            informacion=myform.cleaned_data
            perro = Perro(nombre=informacion["nombre"], datos=informacion["datos"])
            perro.save()
            return render(request,"MisPerros/inicio.html")
    else:
        myform = PerroFormulario()
    
    return render(request,"MisPerros/PerroFormulario.html", {"myform":myform})

def SocioForm(request):
    if request.method == "POST":
        myform1=SocioFormulario(request.POST)
        print(myform1)

        if myform1.is_valid:
            informacion=myform1.cleaned_data
            socio = Socio(nombre=informacion["nombre"], categoria=informacion["categoria"])
            socio.save()
            return render(request,"MisPerros/inicio.html")
    else:
        myform1 = SocioFormulario()
    
    return render(request,"MisPerros/SocioFormulario.html", {"myform1":myform1})

def HogarTemporalForm(request):
    if request.method == "POST":
        myform2=HogarTemporalFormulario(request.POST)
        print(myform2)

        if myform2.is_valid:
            informacion=myform2.cleaned_data
            hogartemporal = HogarTemporal(ubicacion=informacion["ubicacion"], datoshogar=informacion["datoshogar"])
            hogartemporal.save()
            return render(request,"MisPerros/inicio.html")
    else:
        myform2 = HogarTemporalFormulario()
    
    return render(request,"MisPerros/HogarTemporalFormulario.html", {"myform2":myform2})

def buscarperro(request):
    return render (request, "MisPerros/buscarperro.html")
def buscarperro1(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        perros = Perro.objects.filter(nombre__icontains=nombre)
        return render(request, "MisPerros/resultadoBusquedaperro.html", {"perros":perros, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"

def buscarsocio(request):
    return render (request, "MisPerros/buscarsocio.html")
def buscarsocio1(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        socios = Socio.objects.filter(nombre__icontains=nombre)
        return render(request, "MisPerros/resultadoBusquedasocio.html", {"socios":socios, "nombre":nombre})
    else:
        respuesta = "No enviaste datos" 

def buscarhogar_temporal(request):
    return render (request, "MisPerros/buscarhogar_temporal.html")
def buscarhogar_temporal1(request):
    if request.GET["ubicacion"]:
        ubicacion = request.GET['ubicacion']
        hogar_temporals = HogarTemporal.objects.filter(ubicacion__icontains=ubicacion)
        return render(request, "MisPerros/resultadoBusquedahogar_temporal.html", {"hogar_temporals":hogar_temporals, "ubicacion":ubicacion})
    else:
        respuesta = "No enviaste datos" 