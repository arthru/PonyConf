# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='talk',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cfp.TalkCategory', verbose_name='Intervention kind'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Title'),
        ),
    ]