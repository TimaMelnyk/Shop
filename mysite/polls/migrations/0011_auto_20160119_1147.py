# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 09:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160119_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 11, 47, 7, 722277), verbose_name='Time'),
        ),
    ]
