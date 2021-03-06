# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 20:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20160121_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(default=23, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default=23, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.CharField(default='USER', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='vkId',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 22, 38, 27, 301455), verbose_name='Time'),
        ),
    ]
