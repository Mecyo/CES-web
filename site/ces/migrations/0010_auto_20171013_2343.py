# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ces', '0009_auto_20171012_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='profileName',
            new_name='perfilUsuario_id',
        ),
    ]
