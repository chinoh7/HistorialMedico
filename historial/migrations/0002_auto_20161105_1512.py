# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Padecimientos',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='direccion',
        ),
        migrations.AddField(
            model_name='doctor',
            name='direccion',
            field=models.CharField(max_length=100, default=datetime.datetime(2016, 11, 5, 21, 11, 36, 865765, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='padecimientos',
            field=models.ManyToManyField(to='historial.Doctor', through='historial.Padecimiento'),
        ),
        migrations.AddField(
            model_name='padecimiento',
            name='tratamiento',
            field=models.CharField(max_length=60, default=-2010),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='apellido',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
