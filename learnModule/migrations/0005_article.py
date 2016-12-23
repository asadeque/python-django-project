# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0004_auto_20161007_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
