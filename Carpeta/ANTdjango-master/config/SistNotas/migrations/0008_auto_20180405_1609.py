# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-05 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SistNotas', '0007_auto_20180405_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='alumnos',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='profesores',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='id_materia',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
    ]