# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0008_auto_20161121_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='pacientes',
        ),
    ]
