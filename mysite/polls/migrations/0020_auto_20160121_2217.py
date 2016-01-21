# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 20:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20160121_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vkId',
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 22, 17, 10, 612641), verbose_name='Time'),
        ),
    ]
