# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-10 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20161005_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='label',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
