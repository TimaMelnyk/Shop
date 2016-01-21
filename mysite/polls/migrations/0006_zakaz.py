# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 14:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_category_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Purchaser')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('zakaz', models.CharField(max_length=255, verbose_name='Things')),
                ('summa', models.ImageField(default=0, upload_to=b'', verbose_name='Amount')),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 1, 17, 14, 46, 31, 565506), verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
