from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from MisPerros.models import *
from MisPerros.forms import PerroFormulario, SocioFormulario, HogarTemporalFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def menu(request):
    return render(request,"MisPerros/menu.html")
def editarperfil2(request):
    return render(request,"MisPerros/editarperfil2.html")
@login_required
def inicio(request):
    if request.user.is_authenticated == True: #Si el usuario está logueado, pido la foto de avatar
        return render(request, "MisPerros/inicio.html")
    else:
        return render(request, "MisPerros/inicio.html") #Caso contrario, solo renderizo la página de inicio en este caso
@login_required
def perro(request):
    return render(request,"MisPerros/perro.html")
@login_required
def socio(request):
    return render(request,"MisPerros/socio.html")
@login_required
def hogartemporal(request):
    return render(request,"MisPerros/hogartemporal.html")
@login_required
def PerroForm(request):
    if request.method == "POST":
        myform=PerroFormulario(request.POST)
        print(myform)

        if myform.is_valid:
            informacion=myform.cleaned_data
            perro = Perro(nombre=informacion["nombre"], datos=informacion["datos"],img=informacion["img"],sexo=informacion["sexo"])
            perro.save()
            return render(request,"MisPerros/inicio.html")
    else:
        myform = PerroFormulario()
    
    return render(request,"MisPerros/PerroFormulario.html", {"myform":myform})
@login_required
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
@login_required
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
@login_required
def buscarperro(request):
    return render (request, "MisPerros/buscarperro.html")
@login_required
def buscarperro1(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        perros = Perro.objects.filter(nombre__icontains=nombre)
        return render(request, "MisPerros/resultadoBusquedaperro.html", {"perros":perros, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"
@login_required
def buscarsocio(request):
    return render (request, "MisPerros/buscarsocio.html")
@login_required
def buscarsocio1(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        socios = Socio.objects.filter(nombre__icontains=nombre)
        return render(request, "MisPerros/resultadoBusquedasocio.html", {"socios":socios, "nombre":nombre})
    else:
        respuesta = "No enviaste datos" 
@login_required
def buscarhogar_temporal(request):
    return render (request, "MisPerros/buscarhogar_temporal.html")
@login_required
def buscarhogar_temporal1(request):
    if request.GET["ubicacion"]:
        ubicacion = request.GET['ubicacion']
        hogar_temporals = HogarTemporal.objects.filter(ubicacion__icontains=ubicacion)
        return render(request, "MisPerros/resultadoBusquedahogar_temporal.html", {"hogar_temporals":hogar_temporals, "ubicacion":ubicacion})
    else:
        respuesta = "No enviaste datos" 

class PerroList(ListView):
    model = Perro
    template_name = "MisPerros/perro_list.html"   
class PerroDetalle(DetailView):
    model = Perro
    template_name = "MisPerros/perro_detalle.html" 
    
class PerroCreacion(CreateView):
    model = Perro
    success_url = "/"
    fields = ['nombre', 'datos','img','sexo']
class PerroUpdate(UpdateView):
    model = Perro
    success_url = "/perro/list"
    fields = ['nombre', 'datos','img','sexo']   
class PerroDelete(DeleteView):
    model = Perro
    success_url = "/perro/list"
class SocioList(ListView):
    model = Socio
    template_name = "MisPerros/socio_list.html" 
class SocioDetalle(DetailView):
    model = Socio
    template_name = "MisPerros/socio_detalle.html"  
class SocioCreacion(CreateView):
    model = Socio
    success_url = "/"
    fields = ['nombre', 'categoria']
class SocioUpdate(UpdateView):
    model = Socio
    success_url = "/socio/list"
    fields = ['nombre', 'categoria']   
class SocioDelete(DeleteView):
    model = Socio
    success_url = "/socio/list"
class HogarTemporalList(ListView):
    model = HogarTemporal
    template_name = "MisPerros/hogartemporal_list.html"  
class HogarTemporalDetalle(DetailView):
    model = HogarTemporal
    template_name = "MisPerros/hogartemporal_detalle.html"   
class HogarTemporalCreacion(CreateView):
    model = HogarTemporal
    success_url = "/MisPerros/hogar/list"
    fields = ['ubicacion', 'datoshogar']
class HogarTemporalUpdate(UpdateView):
    model = HogarTemporal
    success_url = "/hogar/list"
    fields = ['ubicacion', 'datoshogar']   
class HogarTemporalDelete(DeleteView):
    model = HogarTemporal
    success_url = "/hogar/list"    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)                
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "MisPerros/menu.html", {"mensaje": "Usuario Creado"})    
    else:
        form = UserCreationForm()
    return render(request, "MisPerros/register.html", {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(username=usuario,password=contra)
            if user is not None:
                login(request,user)
                return render(request,"MisPerros/inicio.html")
            else:
                return render(request,"MisPerros/menu.html", {"mensaje":"Parece que no has escrito correctamente tus datos, intente nuevamente:"})
        else:
                return render(request,"MisPerros/menu.html", {"mensaje":"Parece que no has escrito correctamente tus datos, intente nuevamente:"})
    form=AuthenticationForm()
    return render(request,"MisPerros/login.html",{'form':form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        usuario.delete()
        miFormulario = UserEditForm(request.POST)     
        if miFormulario.is_valid():
            username = miFormulario.cleaned_data['username']
            miFormulario.save()
            return render(request, "MisPerros/editarperfil2.html",{"mensaje":"Datos modificados correctamente, por favor ingrese con su nuevo usuario"})
    else:

        miFormulario = UserEditForm()
    return render(request, "MisPerros/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



