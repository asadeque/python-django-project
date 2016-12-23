# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-createdDate', '-updatedDate']},
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
