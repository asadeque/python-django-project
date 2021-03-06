# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learnModule', '0041_auto_20161208_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('imageURL', models.ImageField(blank=True, upload_to='staticfiles/learnModule/images')),
                ('body', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.IntegerField(default=0)),
                ('storyType', models.CharField(choices=[('0', 'None'), ('1', 'Ugly'), ('2', 'Bad'), ('3', 'Good')], default=0, max_length=2)),
                ('community', models.CharField(blank=True, max_length=200, null=True)),
                ('involvedCompany', models.CharField(blank=True, max_length=200, null=True)),
                ('opinionGood', models.CharField(blank=True, max_length=500, null=True)),
                ('opinionBad', models.CharField(blank=True, max_length=500, null=True)),
                ('opinionUnknown', models.CharField(blank=True, max_length=500, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedDate', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Country')),
                ('language', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Language')),
            ],
        ),
        migrations.CreateModel(
            name='StoryChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('imageURL', models.ImageField(blank=True, null=True, upload_to='staticfiles/learnModule/images')),
                ('imageCaption', models.CharField(blank=True, max_length=500, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedDate', models.DateTimeField(auto_now=True, null=True)),
                ('language', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='learnModule.Language')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Story')),
            ],
        ),
    ]
