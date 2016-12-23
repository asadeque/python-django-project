# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0021_auto_20161021_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Quiz'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Course'),
        ),
    ]