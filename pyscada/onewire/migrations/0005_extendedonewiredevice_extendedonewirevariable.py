# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0041_update_protocol_id'),
        ('onewire', '0004_auto_20170405_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedOneWireDevice',
            fields=[
            ],
            options={
                'verbose_name': 'OneWire Device',
                'proxy': True,
                'verbose_name_plural': 'OneWire Devices',
                'indexes': [],
            },
            bases=('pyscada.device',),
        ),
        migrations.CreateModel(
            name='ExtendedOneWireVariable',
            fields=[
            ],
            options={
                'verbose_name': 'OneWire Variable',
                'proxy': True,
                'verbose_name_plural': 'OneWire Variable',
                'indexes': [],
            },
            bases=('pyscada.variable',),
        ),
    ]