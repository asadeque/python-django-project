# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20161124_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquiz',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Choice'),
        ),
    ]
