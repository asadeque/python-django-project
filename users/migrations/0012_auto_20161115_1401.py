# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20161115_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
