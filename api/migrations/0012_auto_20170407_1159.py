# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170407_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metering',
            name='pm01',
            field=models.IntegerField(blank=True, default=None, help_text='PM 0.1 in ug/m^3', null=True),
        ),
        migrations.AlterField(
            model_name='metering',
            name='pm10',
            field=models.IntegerField(help_text='PM 10 in ug/m^3'),
        ),
        migrations.AlterField(
            model_name='metering',
            name='pm25',
            field=models.IntegerField(help_text='PM 2.5 in ug/m^3'),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='pm01',
            field=models.IntegerField(blank=True, default=None, help_text='PM 0.1 in ug/m^3', null=True),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='pm10',
            field=models.IntegerField(help_text='PM 10 in ug/m^3'),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='pm25',
            field=models.IntegerField(help_text='PM 2.5 in ug/m^3'),
        ),
    ]
