# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0029_auto_20161109_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='srNo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
