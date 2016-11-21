# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0007_doctor_usuario_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('enfermedad', models.ForeignKey(to='historial.Enfermedad')),
                ('paciente', models.ForeignKey(to='historial.Paciente')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='pacientes',
            field=models.ManyToManyField(through='historial.Consulta', to='historial.Paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='enfermedades',
            field=models.ManyToManyField(through='historial.Padecimiento', to='historial.Enfermedad'),
        ),
    ]
