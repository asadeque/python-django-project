# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_user_profilehighlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
