# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 22:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0048_remove_summary_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='language',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
