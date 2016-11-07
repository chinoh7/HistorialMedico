# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historial', '0004_auto_20161105_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
    ]
