# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0003_auto_20161105_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='descripcion',
            new_name='descripcion_padecimiento',
        ),
    ]
