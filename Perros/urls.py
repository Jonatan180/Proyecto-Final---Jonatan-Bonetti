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
from django.urls import path, include
from MisPerros import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", views.inicio, name="inicio"),
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
    path('perro/list', views.PerroList.as_view(), name='Listperro'),
    path(r'^perro(?P<pk>\d+)$', views.PerroDetalle.as_view(), name='Detailperro'),
    path('perro/Newperro', views.PerroCreacion.as_view(), name='Newperro'),
    path(r'^editarperro/(?P<pk>\d+)$', views.PerroUpdate.as_view(), name='Editperro'),
    path(r'^borrarperro/(?P<pk>\d+)$', views.PerroDelete.as_view(), name='Deleteperro'),
    path('socio/list', views.SocioList.as_view(), name='Listsocio'),
    path(r'^socio(?P<pk>\d+)$', views.SocioDetalle.as_view(), name='Detailsocio'),
    path('socio/Newsocio', views.SocioCreacion.as_view(), name='Newsocio'),
    path(r'^editarsocio/(?P<pk>\d+)$', views.SocioUpdate.as_view(), name='Editsocio'),
    path(r'^borrarsocio/(?P<pk>\d+)$', views.SocioDelete.as_view(), name='Deletesocio'),
    path('hogar/list', views.HogarTemporalList.as_view(), name='Listhogar'),
    path(r'^hogar(?P<pk>\d+)$', views.HogarTemporalDetalle.as_view(), name='Detailhogar'),
    path(r'^nuevo$', views.HogarTemporalCreacion.as_view(), name='Newhogar'),
    path(r'^editarhogar/(?P<pk>\d+)$', views.HogarTemporalUpdate.as_view(), name='Edithogar'),
    path(r'^borrarhogar/(?P<pk>\d+)$', views.HogarTemporalDelete.as_view(), name='Deletehogar'),
    path('login/',views.login_request,name='login'),
    path('', views.menu, name="menu"),
    path('logout/', LogoutView.as_view(template_name='MisPerros/menu.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('register/', views.register, name='register'),
    path('editarperfil2/', views.editarperfil2, name='editarperfil2'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
