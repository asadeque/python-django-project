# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 21:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnModule', '0041_auto_20161208_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='country',
        ),
        migrations.RemoveField(
            model_name='article',
            name='language',
        ),
        migrations.RemoveField(
            model_name='articlechild',
            name='article',
        ),
        migrations.RemoveField(
            model_name='articlechild',
            name='language',
        ),
        migrations.RemoveField(
            model_name='author',
            name='country',
        ),
        migrations.RemoveField(
            model_name='author',
            name='language',
        ),
        migrations.RemoveField(
            model_name='contenttype',
            name='language',
        ),
        migrations.RemoveField(
            model_name='copyright',
            name='language',
        ),
        migrations.RemoveField(
            model_name='format',
            name='language',
        ),
        migrations.RemoveField(
            model_name='howtowork',
            name='language',
        ),
        migrations.RemoveField(
            model_name='informationfor',
            name='language',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='language',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='resourcetype',
            name='language',
        ),
        migrations.RemoveField(
            model_name='source',
            name='language',
        ),
        migrations.RemoveField(
            model_name='writtenby',
            name='language',
        ),
        migrations.RemoveField(
            model_name='writtenfor',
            name='language',
        ),
        migrations.RemoveField(
            model_name='content',
            name='complexity',
        ),
        migrations.RemoveField(
            model_name='content',
            name='contentType',
        ),
        migrations.RemoveField(
            model_name='content',
            name='copyRight',
        ),
        migrations.RemoveField(
            model_name='content',
            name='country',
        ),
        migrations.RemoveField(
            model_name='content',
            name='format',
        ),
        migrations.RemoveField(
            model_name='content',
            name='informationFor',
        ),
        migrations.RemoveField(
            model_name='content',
            name='resourceType',
        ),
        migrations.RemoveField(
            model_name='content',
            name='source',
        ),
        migrations.RemoveField(
            model_name='content',
            name='writtenBy',
        ),
        migrations.RemoveField(
            model_name='content',
            name='writtenFor',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleChild',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='ContentType',
        ),
        migrations.DeleteModel(
            name='CopyRight',
        ),
        migrations.DeleteModel(
            name='Format',
        ),
        migrations.DeleteModel(
            name='HowToWork',
        ),
        migrations.DeleteModel(
            name='InformationFor',
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
        migrations.DeleteModel(
            name='ResourceType',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='WrittenBy',
        ),
        migrations.DeleteModel(
            name='WrittenFor',
        ),
    ]
