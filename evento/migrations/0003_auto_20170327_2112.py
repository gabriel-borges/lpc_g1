# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20170327_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigocientifico',
            name='autores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Autor'),
        ),
    ]
