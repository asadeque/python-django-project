# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0011_auto_20161017_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('imageURL', models.ImageField(blank=True, upload_to=b'Image/HowToWork')),
                ('body', models.TextField(blank=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
