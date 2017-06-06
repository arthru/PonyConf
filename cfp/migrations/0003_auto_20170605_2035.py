# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0002_auto_20170605_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description of your talk'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='notes',
            field=models.TextField(blank=True, help_text='If you have any constraint or if you have anything that may help you to select your talk, like a video or slides of your talk, please write it down here', verbose_name='Message to organizers'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Talk Title'),
        ),
    ]