# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0022_auto_20161101_2117'),
        ('users', '0002_auto_20161101_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='courseID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Course'),
        ),
    ]
