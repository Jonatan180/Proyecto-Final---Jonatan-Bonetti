"""Perros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MisPerros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("perro/", views.perro, name="perro"),
    path("socio/", views.socio, name="socio"),
    path("hogartemporal/", views.hogartemporal, name="hogartemporal"),
    path("PerroForm/", views.PerroForm, name="PerroForm"),
    path("SocioForm/", views.SocioForm, name="SocioForm"),
    path("HogarTemporalForm/", views.HogarTemporalForm, name="HogarTemporalForm"),
    path("buscarperro/", views.buscarperro, name="buscarperro"),
    path("buscarperro1/", views.buscarperro1),
    path("buscarsocio/", views.buscarsocio, name="buscarsocio"),
    path("buscarsocio1/", views.buscarsocio1),
    path("buscarhogar_temporal/", views.buscarhogar_temporal, name="buscarhogar_temporal"),
    path("buscarhogar_temporal1/", views.buscarhogar_temporal1),
]
