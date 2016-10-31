# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Padecimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=120)),
                ('fecha_padecimiento', models.DateField()),
                ('doctor', models.ForeignKey(to='historial.Doctor')),
                ('paciente', models.ForeignKey(to='historial.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='Padecimientos',
            field=models.ManyToManyField(to='historial.Paciente', through='historial.Padecimiento'),
        ),
    ]
