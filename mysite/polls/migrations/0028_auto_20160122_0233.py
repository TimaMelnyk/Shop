# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 00:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20160122_0215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bootik',
            new_name='Shop',
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Shop', 'verbose_name_plural': 'Shopes'},
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 2, 33, 13, 944743), verbose_name='Time'),
        ),
    ]
