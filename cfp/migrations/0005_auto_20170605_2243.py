# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cfp', '0004_talk_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talkcategory',
            options={'ordering': ('pk',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='conference',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='conference',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='talk',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cfp.TalkCategory', verbose_name='Talk Category'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='video_licence',
            field=models.CharField(choices=[('CC-Zero CC-BY', 'CC-Zero CC-BY'), ('CC-BY-SA', 'CC-BY-SA'), ('CC-BY-ND', 'CC-BY-ND'), ('CC-BY-NC', 'CC-BY-NC'), ('CC-BY-NC-SA', 'CC-BY-NC-SA'), ('CC-BY-NC-ND', 'CC-BY-NC-ND')], default='CC-BY-SA', max_length=10, verbose_name='Video licence'),
        ),
    ]