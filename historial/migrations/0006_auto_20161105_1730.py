# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0005_padecimiento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Padecimiento',
            new_name='Enfermedad',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='padecimientos',
        ),
        migrations.AddField(
            model_name='consulta',
            name='enfermedad',
            field=models.ForeignKey(default=-2010, to='historial.Enfermedad'),
            preserve_default=False,
        ),
    ]
