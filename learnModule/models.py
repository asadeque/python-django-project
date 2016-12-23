from django.db import models
from django.core.urlresolvers import reverse

import datetime

# Create your models here
CONTENTFOR = (
        ('0', 'None'),
        ('1', 'FPIC'),
        ('2', 'Consultation'),
)

HIGHLIGHT = (
        ('0', 'None'),
        ('1', 'Information'),
        ('2', 'Toolkit'),
)

class Language(models.Model):
    name = models.CharField(max_length=200)
    codeFileName = models.CharField(max_length=50, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class SubMenuLang(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Complexity(models.Model):
    level = models.IntegerField(default=1)
    title = models.CharField(max_length=50, default='Simple')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images')
    contentFor = models.CharField(max_length=2, choices=CONTENTFOR, default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    complexity = models.ForeignKey(Complexity, on_delete=models.CASCADE, default=1)
    duration = models.IntegerField(blank=True,null=True)
    recommend = models.IntegerField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    srNo = models.IntegerField(blank=True,null=True)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

class ContentStyle(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=100)
    keywordsContent = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    contentFor = models.CharField(max_length=2, choices=CONTENTFOR, default=0)
    highlight = models.CharField(max_length=2, choices=HIGHLIGHT, default=0)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True)
    audio_file = models.URLField(blank=True)
    video_file = models.FileField(upload_to='staticfiles/learnModule/images', blank=True)
    file_content = models.FileField(blank=True, upload_to='staticfiles/learnModule/images')
    lengthInMB = models.IntegerField(blank=True,null=True)
    sizeInPages = models.IntegerField(blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)
    author = models.CharField(max_length=500, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=2)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    srNo = models.IntegerField(blank=True,null=True)
    style = models.ForeignKey(ContentStyle, on_delete=models.CASCADE, default=1)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
            return reverse("learnModule:contentHome", kwargs={"id":self.id})


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, default=59)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s' % self.content


class Question(models.Model):
    questionText = models.CharField(max_length=250)
    questionDescription = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.questionText


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=250)
    isAnswer = models.BooleanField(default=0)
    answerDescription =  models.CharField(max_length=500, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s %s %d' % (self.question, self.choiceText, self.isAnswer)


class CheckList(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    srNo = models.IntegerField(blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    weightValue = models.IntegerField(blank=True,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
         return '%s %s' % (self.content, self.title)


class Summary(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
         return '%s %s' % (self.content, self.title)


class SummaryChild(models.Model):
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    srNo = models.IntegerField(blank=True,null=True)
    advice = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
         return '%s %s' % (self.summary, self.advice)


class Finish(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    imageURL = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True)
    congratWords = models.CharField(max_length=200)
    suggestion = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=2)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
         return '%s %s' % (self.content, self.congratWords)
