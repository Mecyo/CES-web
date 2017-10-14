# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ces', '0007_auto_20171012_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataReserva', models.DateTimeField(blank=True, null=True)),
                ('objeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.Objeto')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ces.Usuario')),
            ],
            options={
                'verbose_name_plural': 'Reservas',
                'verbose_name': 'Reserva',
            },
        ),
    ]
