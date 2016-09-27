# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Importe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('coste', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateField()),
                ('pago', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('documento', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(blank=True, max_length=50)),
                ('curso', models.CharField(max_length=10)),
                ('fechaInscripcion', models.DateField()),
                ('socioCompleto', models.IntegerField(choices=[(1, 'completo'), (0, 'incompleto')], default=0)),
                ('usuarioCampus', models.CharField(blank=True, max_length=50)),
                ('epecialidad', models.IntegerField(choices=[(0, 'ninguna'), (1, 'informatica'), (2, 'electronica')], default=0)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='socio',
            field=models.ForeignKey(to='aplicacionSociosCooperativa.Socio'),
        ),
    ]
