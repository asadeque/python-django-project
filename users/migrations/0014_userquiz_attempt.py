# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_usercontentdownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquiz',
            name='attempt',
            field=models.IntegerField(default=1),
        ),
    ]
