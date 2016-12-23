from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import learnModule, library
from library.models import Country
import datetime
# Create your models here.

STORYTYPE = (
        ('0', 'None'),
        ('1', 'Ugly'),
        ('2', 'Bad'),
        ('3', 'Good'),
)

class Story(models.Model):
    title = models.CharField(max_length=200)
    subTitle = models.CharField(max_length=200, blank=True, null=True)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    storyType = models.CharField(max_length=2, choices=STORYTYPE, default=0)
    country = models.ForeignKey(library.models.Country, on_delete=models.CASCADE, blank=True, null=True)
    community = models.CharField(max_length=200, blank=True, null=True)
    involvedCompany = models.CharField(max_length=200, blank=True, null=True)
    opinionGood = models.CharField(max_length=500, blank=True, null=True)
    opinionBad = models.CharField(max_length=500, blank=True, null=True)
    opinionUnknown = models.CharField(max_length=500, blank=True, null=True)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class StoryChild(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True, null=True)
    imageCaption = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title
