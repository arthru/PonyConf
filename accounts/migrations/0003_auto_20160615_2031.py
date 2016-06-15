# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 20:31
from __future__ import unicode_literals

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160615_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='transport',
            field=models.IntegerField(blank=True, choices=[(1, 'train'), (2, 'plane'), (3, 'others')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_token',
            field=models.CharField(default=accounts.utils.generate_user_uid, max_length=12, unique=True),
        ),
    ]
