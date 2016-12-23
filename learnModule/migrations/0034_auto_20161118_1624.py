# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0033_auto_20161118_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleType',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'Ugly'), (b'2', b'Bad'), (b'3', b'Good')], default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='course',
            name='complexity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Complexity'),
        ),
        migrations.AddField(
            model_name='course',
            name='contentFor',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'FPIC'), (b'2', b'Consultation')], default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='recommend',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='content',
            name='contentFor',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'FPIC'), (b'2', b'Consultation')], default=0, max_length=2),
        ),
    ]