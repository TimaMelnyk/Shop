# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 09:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160117_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 11, 20, 29, 835600), verbose_name='Time'),
        ),
    ]
