# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0035_content_highlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='complexity',
            name='title',
            field=models.CharField(default=b'Simple', max_length=50),
        ),
    ]
