from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
import learnModule
from learnModule.models import Language, Complexity, Topic, Course
import datetime
# Create your models here.


LIBRARYFOR = (
        ('0', 'None'),
        ('1', 'FPIC'),
        ('2', 'Consultation'),
)

HIGHLIGHT1 = (
        ('0', 'None'),
        ('1', 'Information'),
        ('2', 'Toolkit'),
)

LIBRARYSTYLE = (
        ('0', 'None'),
        ('1', 'Text'),
        ('2', 'Text & Image'),
        ('3', 'Quiz Boolean'),
        ('4', 'Checklist'),
        ('5', 'Quiz Multiple Choice'),
        ('6', 'Summary'),
        ('7', 'Resources'),
        ('8', 'Finish'),
        ('9', 'Other'),
)


class Country(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class WrittenFor(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class InformationFor(models.Model):
    userType = models.CharField(max_length=100)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.userType


class WrittenBy(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Format(models.Model):
    formatType = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.formatType


class CopyRight(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class ResourceType(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class LibraryType(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Library(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    LibraryType = models.ForeignKey(LibraryType, on_delete=models.CASCADE, default=1)
    libraryFor = models.CharField(max_length=2, choices=LIBRARYFOR, default=0)
    highlight = models.CharField(max_length=2, choices=HIGHLIGHT1, default=0)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True)
    audio_file = models.URLField(blank=True)
    video_file = models.FileField(upload_to='staticfiles/learnModule/images', blank=True)
    file_content = models.FileField(blank=True, upload_to='staticfiles/library/pdf')
    lengthInMB = models.IntegerField(blank=True,null=True)
    sizeInPages = models.IntegerField(blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)
    author = models.CharField(max_length=500, blank=True)
    writtenFor = models.ForeignKey(WrittenFor, on_delete=models.CASCADE, default=1)
    writtenBy = models.ForeignKey(WrittenBy, on_delete=models.CASCADE, default=1)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, default=1)
    complexity = models.ForeignKey(learnModule.models.Complexity, on_delete=models.CASCADE, default=1)
    copyRight = models.ForeignKey(CopyRight, on_delete=models.CASCADE, default=1)
    informationFor = models.ForeignKey(InformationFor, on_delete=models.CASCADE, default=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(learnModule.models.Topic, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(learnModule.models.Course, on_delete=models.CASCADE, blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, default=1)
    resourceType = models.ForeignKey(ResourceType, on_delete=models.CASCADE, default=1)
    language = models.ForeignKey(learnModule.models.Language, on_delete=models.CASCADE, default=2)
    srNo = models.IntegerField(blank=True,null=True)
    style = models.CharField(max_length=2, choices=LIBRARYSTYLE, default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
            return reverse("library:libraryHome", kwargs={"id":self.id})
