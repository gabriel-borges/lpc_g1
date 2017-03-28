from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.

def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/eventoscientificos'>Eventos Cientificos</a></li>
                    <li><a href='/pessoas'>Pessoas</a></li>
                    <li><a href='/autores'>Autores</a></li>
                    <li><a href='/pessoasfisicas'>Pessoas Físicas</a></li>
                    <li><a href='/pessoasjuridicas'>Pessoas Jurídicas</a></li>
                    <li><a href='/artigos'>Artigos</a></li>
                </ul>
            """
    return HttpResponse(html)

# Eventos

def listaEventos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        html += "<h2>" + evento.nome + "</h2>"
        html += "<ul id='evento-" + str(evento.id) + "'>"
        html += "<li><strong>Evento Principal:</strong> " + evento.eventoprincipal + "</li>"
        html += "<li><strong>Sigla:</strong> " + evento.sigla + "</li>"
        html += "<li><strong>Palavras-chave:</strong> " + evento.palavraschave + "</li>"
        html += "<li><strong>Logotipo:</strong> " + evento.logotipo + "</li>"
        html += "<li><strong>Realizador:</strong> " + str(evento.realizador.nome) + "</li>"
        html += "<li><strong>Cidade:</strong>" + evento.cidade + "</li>"
        html += "<li><strong>UF:</strong> " + evento.uf + "</li>"
        html += "<li><strong>CEP:</strong> " + evento.cep + "</li>"
        html += "</ul>"

    return HttpResponse(html)


def eventoEspecifico(request, id):
    html = "<h1>Informações sobre o Evento</h1>"
    evento = Evento.objects.get(pk=id)
    html += "<h2>" + evento.nome + "</h2>"
    html += "<ul id='evento-" + str(evento.id) + "'>"
    html += "<li><strong>Evento Principal:</strong> " + evento.eventoprincipal + "</li>"
    html += "<li><strong>Sigla:</strong> " + evento.sigla + "</li>"
    html += "<li><strong>Palavras-chave:</strong> " + evento.palavraschave + "</li>"
    html += "<li><strong>Logotipo:</strong> " + evento.logotipo + "</li>"
    html += "<li><strong>Realizador:</strong> " + str(evento.realizador.nome) + "</li>"
    html += "<li><strong>Cidade:</strong> " + evento.cidade + "</li>"
    html += "<li><strong>UF:</strong> " + evento.uf + "</li>"
    html += "<li><strong>CEP:</strong> " + evento.cep + "</li>"
    html += "</ul>"

    return HttpResponse(html)

# Eventos Cientificos

def listaEventosCientificos(request):
    html = "<h1>Lista de Eventos Cientificos</h1>"
    lista = EventoCientifico.objects.all()
    for evento in lista:
        html += "<h2>" + str(evento.nome) + "</h2>"
        html += "<ul id='evento-" + str(evento.id) + "'>"
        html += "<li><strong>ISSN:</strong> " + evento.issn + "</li>"
        html += "<li><strong>Evento Principal:</strong> " + str(evento.eventoprincipal) + "</li>"
        html += "<li><strong>Sigla:</strong> " + str(evento.sigla) + "</li>"
        html += "<li><strong>Palavras-chave:</strong> " + str(evento.palavraschave) + "</li>"
        html += "<li><strong>Logotipo:</strong> " + str(evento.logotipo) + "</li>"
        html += "<li><strong>Realizador:</strong> " + str(evento.realizador.nome) + " (" + str(evento.realizador.email) +")</li>"
        html += "<li><strong>Cidade:</strong> " + str(evento.cidade) + "</li>"
        html += "<li><strong>UF:</strong> " + str(evento.uf) + "</li>"
        html += "<li><strong>CEP:</strong> " + str(evento.cep) + "</li>"
        html += "</ul>"

    return HttpResponse(html)


def eventoCientificoEspecifico(request, id):
    html = "<h1>Informações sobre o Evento Cientifico</h1>"
    evento = EventoCientifico.objects.get(evento_ptr_id=id)
    html += "<h2>" + str(evento.nome) + "</h2>"
    html += "<ul id='evento-" + str(evento.id) + "'>"
    html += "<li><strong>ISSN:</strong> " + evento.issn + "</li>"
    html += "<li><strong>Evento Principal:</strong> " + str(evento.eventoprincipal) + "</li>"
    html += "<li><strong>Sigla:</strong> " + str(evento.sigla) + "</li>"
    html += "<li><strong>Palavras-chave:</strong> " + str(evento.palavraschave) + "</li>"
    html += "<li><strong>Logotipo:</strong> " + str(evento.logotipo) + "</li>"
    html += "<li><strong>Realizador:</strong> " + str(evento.realizador.nome) + " (" + str(evento.realizador.email) +")</li>"
    html += "<li><strong>Cidade:</strong> " + str(evento.cidade) + "</li>"
    html += "<li><strong>UF:</strong> " + str(evento.uf) + "</li>"
    html += "<li><strong>CEP:</strong> " + str(evento.cep) + "</li>"
    html += "</ul>"

    return HttpResponse(html)


# Pessoas

def listaPessoas(request):
    html = "<h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    for pessoa in lista:
        html += "<strong>None:</strong> " + pessoa.nome + "<br />"
        html += "<strong>E-mail:</strong> " + pessoa.email + "<br /><br />"

    return HttpResponse(html)


def pessoaEspecifica(request, id):
    html = "<h1>Informações sobre a Pessoa</h1>"
    pessoa = Pessoa.objects.get(pk=id)
    html += "<strong>None:</strong> " + pessoa.nome + "<br />"
    html += "<strong>E-mail:</strong> " + pessoa.email

    return HttpResponse(html)


# Pessoas Físicas

def listaPessoasFisicas(request):
    html = "<h1>Lista de Pessoas Físicas</h1>"
    lista = PessoaFisica.objects.all()
    for pessoa in lista:
        html += "<strong>None:</strong> " + str(pessoa.nome) + "<br />"
        html += "<strong>E-mail:</strong> " + str(pessoa.email) + "<br />"
        html += "<strong>CPF:</strong> " + pessoa.cpf + "<br /><br />"

    return HttpResponse(html)


def pessoaFisicaEspecifica(request, id):
    html = "<h1>Informações sobre a Pessoa Física</h1>"
    pessoa = PessoaFisica.objects.get(pessoa_ptr_id=id)
    html += "<strong>None:</strong> " + str(pessoa.nome) + "<br />"
    html += "<strong>E-mail:</strong> " + str(pessoa.email) + "<br />"
    html += "<strong>CPF:</strong> " + pessoa.cpf + "<br /><br />"

    return HttpResponse(html)


# Pessoas Jurídicas

def listaPessoasJuridicas(request):
    html = "<h1>Lista de Pessoas Jurídicas</h1>"
    lista = PessoaJuridica.objects.all()
    for pessoa in lista:
        html += "<strong>None:</strong> " + str(pessoa.nome) + "<br />"
        html += "<strong>E-mail:</strong> " + str(pessoa.email) + "<br />"
        html += "<strong>CNPJ:</strong> " + pessoa.cnpj + "<br />"
        html += "<strong>Razão Social:</strong> " + pessoa.razaosocial + "<br /><br />"

    return HttpResponse(html)


def pessoaJuridicaEspecifica(request, id):
    html = "<h1>Informações sobre a Pessoa Jurídica</h1>"
    pessoa = PessoaJuridica.objects.get(pessoa_ptr_id=id)
    html += "<strong>None:</strong> " + str(pessoa.nome) + "<br />"
    html += "<strong>E-mail:</strong> " + str(pessoa.email) + "<br />"
    html += "<strong>CNPJ:</strong> " + pessoa.cnpj + "<br />"
    html += "<strong>Razão Social:</strong> " + pessoa.razaosocial + "<br /><br />"

    return HttpResponse(html)


# Artigos

def listaArtigos(request):
    html = "<h1>Lista de Artigos</h1>"
    lista = ArtigoCientifico.objects.all()
    for artigo in lista:
        html += "<strong>Título:</strong> " + artigo.titulo + "<br />"
        html += "<strong>Autor:</strong> " + str(artigo.autores.nome) + "<br /><br />"

    return HttpResponse(html)

def artigoEspecifico(request, id):
    html = "<h1>Informações sobre o Artigo</h1>"
    artigo = ArtigoCientifico.objects.get(pk=id)
    html += "<strong>Título:</strong> " + artigo.titulo + "<br />"
    html += "<strong>Autor:</strong> " + str(artigo.autores.nome) + "<br /><br />"

    return HttpResponse(html)


# Autores

def listaAutores(request):
    html = "<h1>Lista de Autores</h1>"
    lista = Autor.objects.all()
    for autor in lista:
        html += "<strong>Nome:</strong> " + str(autor.nome) + "<br />"
        html += "<strong>Currículo:</strong> " + str(autor.curriculo) + "<br />"
        html += "<strong>Artigos (ID):</strong> " + str(autor.artigos) + "<br /><br />"

    return HttpResponse(html)

def autorEspecifico(request, id):
    html = "<h1>Informações sobre o Autor</h1>"
    autor = Autor.objects.get(pk=id)
    html += "<strong>Nome:</strong> " + str(autor.nome) + "<br />"
    html += "<strong>Currículo:</strong> " + str(autor.curriculo) + "<br />"
    html += "<strong>Artigos (ID):</strong> " + str(autor.artigos) + "<br /><br />"

    return HttpResponse(html)


# Participante

def listaParticipantes(request):
    html = "<h1>Lista de Participantes</h1>"
    lista = Participantes.objects.all()
    for participantes in lista:
        html += "<strong>None:</strong> " + str(participante.nome) + "<br />"
        html += "<strong>E-mail:</strong> " + str(participante.email) + "<br />"
        html += "<strong>CPF:</strong> " + str(participante.cpf) + "<br />"
        html += "<strong>Tipo de Inscrição:</strong> " + str(participante.tipoinscricao) + "<br />"
        html += "<strong>Evento Inscrito:</strong> " + str(participante.evento) + "<br /><br />"

    return HttpResponse(html)
