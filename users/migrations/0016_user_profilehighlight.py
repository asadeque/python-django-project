# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20161118_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileHighlight',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
