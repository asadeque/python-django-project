# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0017_auto_20161021_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='keywords',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
