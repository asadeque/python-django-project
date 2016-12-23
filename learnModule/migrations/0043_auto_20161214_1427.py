# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0042_auto_20161209_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Language')),
            ],
        ),
    ]