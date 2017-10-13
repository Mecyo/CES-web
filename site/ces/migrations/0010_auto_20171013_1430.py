# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 17:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ces', '0009_auto_20171012_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='objeto_id',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='usuario_id',
        ),
        migrations.RenameField(
            model_name='transferencia',
            old_name='destinatario',
            new_name='movimentacao_id_destino',
        ),
        migrations.RenameField(
            model_name='transferencia',
            old_name='remetente',
            new_name='movimentacao_id_origem',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
