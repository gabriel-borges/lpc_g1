"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from evento.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', inicio, name='inicio'),
    url(r'^eventos/', listaEventos),
    url(r'^evento/([0-9]{1})', eventoEspecifico),
    url(r'^eventoscientificos/', listaEventosCientificos),
    url(r'^eventocientifico/([0-9]{1})', eventoCientificoEspecifico),
    url(r'^pessoas/', listaPessoas),
    url(r'^pessoa/([0-9]{1})', pessoaEspecifica),
    url(r'^pessoasfisicas/', listaPessoasFisicas),
    url(r'^pessoafisica/([0-9]{1})', pessoaFisicaEspecifica),
    url(r'^pessoasjuridicas/', listaPessoasJuridicas),
    url(r'^pessoajuridica/([0-9]{1})', pessoaJuridicaEspecifica),
    url(r'^artigos/', listaArtigos),
    url(r'^artigo/([0-9]{1})', artigoEspecifico),
    url(r'^autores/', listaAutores),
    url(r'^autor/([0-9]{1})', autorEspecifico),
]
