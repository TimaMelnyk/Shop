# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20160119_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 12, 48, 49, 972088), verbose_name='Time'),
        ),
    ]
