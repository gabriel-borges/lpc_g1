# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('eventoprincipal', models.CharField(max_length=200, verbose_name='eventoprincipal')),
                ('sigla', models.CharField(max_length=10, verbose_name='sigla')),
                ('dataEHoraDeInicio', models.DateField(verbose_name='dataEHoraDeInicio')),
                ('palavraschave', models.CharField(max_length=100, verbose_name='palavras-chave')),
                ('logotipo', models.CharField(max_length=100, verbose_name='logotipo')),
                ('cidade', models.CharField(max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(max_length=100, verbose_name='uf')),
                ('cep', models.CharField(max_length=10, verbose_name='cep')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('curriculo', models.CharField(max_length=200, verbose_name='curriculo')),
                ('artigos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.AtigoCientifico')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Evento')),
                ('issn', models.CharField(max_length=20, verbose_name='issn')),
            ],
            bases=('evento.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cpf', models.CharField(max_length=20, verbose_name='cpf')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Pessoa')),
                ('cnjp', models.CharField(max_length=20, verbose_name='cnpj')),
                ('razaosocial', models.CharField(max_length=100, verbose_name='razao social')),
            ],
            bases=('evento.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Pessoa'),
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('pessoafisica_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.PessoaFisica')),
                ('dataEHoraDeInscricao', models.DateField(verbose_name='dataEHoraDeInscricao')),
                ('tipoinscricao', models.CharField(max_length=15, verbose_name='tipo de inscricao')),
            ],
            bases=('evento.pessoafisica',),
        ),
        migrations.AddField(
            model_name='atigocientifico',
            name='autores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.EventoCientifico'),
        ),
    ]
