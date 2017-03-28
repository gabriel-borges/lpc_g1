from django.db import models
from django.utils import timezone

# Create your models here.

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoprincipal = models.CharField('eventoprincipal', max_length=200)
    sigla = models.CharField('sigla', max_length=10)
    dataEHoraDeInicio = models.DateField('dataEHoraDeInicio')
    palavraschave = models.CharField('palavras-chave', max_length=100)
    logotipo = models.CharField('logotipo', max_length=100)
    realizador = models.ForeignKey('Pessoa')
    cidade = models.CharField('cidade', max_length=100)
    uf = models.CharField('uf', max_length=100)
    cep = models.CharField('cep', max_length=10)

    def __str__(self):
        return '{}'.format(self.nome)

class EventoCientifico(Evento):
    issn = models.CharField('issn', max_length=20)

    def __str__(self):
        return '{}'.format(self.issn)



class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    autores = models.ForeignKey('Autor')

    def __str__(self):
        return '{}'.format(self.titulo)



class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)

    def __str__(self):
        return '{}{}'.format(self.nome, self.email)


class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=200)
    artigos = models.CharField('idsArtigos', max_length=200)

    def __str__(self):
        return '{}'.format(self.curriculo)


class PessoaJuridica(Pessoa):
    cnpj = models.CharField('cnpj', max_length=20)
    razaosocial = models.CharField('razao social', max_length=100)

    def __str__(self):
        return '{}'.format(self.cnjp)


class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=20)

    def __str__(self):
        return '{}'.format(self.cpf)


class Participante(PessoaFisica):
    dataEHoraDeInscricao = models.DateField('dataEHoraDeInscricao')
    tipoinscricao = models.CharField('tipo de inscricao', max_length=15)


    def __str__(self):
        return '{}'.format(self.tipoinscricao)
