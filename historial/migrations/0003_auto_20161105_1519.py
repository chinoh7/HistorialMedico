# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0002_auto_20161105_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=120)),
                ('fecha_padecimiento', models.DateField()),
                ('tratamiento', models.CharField(max_length=60)),
                ('doctor', models.ForeignKey(to='historial.Doctor')),
            ],
        ),
        migrations.RemoveField(
            model_name='padecimiento',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='padecimiento',
            name='paciente',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='padecimientos',
            field=models.ManyToManyField(to='historial.Doctor', through='historial.Consulta'),
        ),
        migrations.DeleteModel(
            name='Padecimiento',
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(to='historial.Paciente'),
        ),
    ]
