# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160115_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
