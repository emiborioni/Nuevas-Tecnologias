# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-05 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistNotas', '0004_auto_20180405_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='alumnos',
            field=models.ManyToManyField(blank=True, null=True, to='SistNotas.Alumno'),
        ),
    ]
