from __future__ import unicode_literals

from django.db import models
from passlib.hash import pbkdf2_sha256
from django.core.urlresolvers import reverse

import library, learnModule
from library.models import Library


class UserType(models.Model):
    type = models.CharField(max_length=200)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.type


class User(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=100, blank=True, null=True)
    userName = models.CharField(max_length=40,blank=True, null=True)
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='staticfiles/learnModule/images', blank=True, null=True)
    profileHighlight = models.CharField(max_length=256, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s' % (self.email)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    def get_absolute_url(self):
        return reverse("users:profile_detail", kwargs={"id":self.id})


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(learnModule.models.Course, on_delete=models.CASCADE, blank=True, null=True)
    isCompleted = models.BooleanField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='LCR')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.course, self.type)


class UserTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(learnModule.models.Topic, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='LT')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.topic, self.type)


class UserContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(learnModule.models.Content, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='LC')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.content, self.type)

    def get_absolute_url(self):
            return reverse("learnModule:contentHome", kwargs={"id":self.content_id})


class UserQuiz(models.Model):
    quiz = models.ForeignKey(learnModule.models.Quiz, on_delete=models.CASCADE)
    attempt = models.IntegerField(default=1)
    question = models.ForeignKey(learnModule.models.Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(learnModule.models.Choice, on_delete=models.CASCADE, blank=True, null=True)
    isCorrect = models.BooleanField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return '%s %s %d %s %s' % (self.user, self.question, self.attempt, self.quiz, self.choice)


class UserChecklist(models.Model):
    checkList = models.ForeignKey(learnModule.models.CheckList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isChecked = models.BooleanField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.checkList, self.isChecked)


class UserResourceDownload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(library.models.Library, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    type = models.CharField(max_length=5, default='DR')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.library, self.type)



class UserFavouriteContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(learnModule.models.Content, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='FC')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.content, self.type)

    def get_absolute_url(self):
            return reverse("learnModule:contentHome", kwargs={"id":self.content_id})


class UserFavouriteResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(library.models.Library, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='FR')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.library, self.type)

    def get_absolute_url(self):
            return reverse("library:libraryDetails", kwargs={"id":self.library_id})


class UserFavouriteCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(learnModule.models.Course, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)
    type = models.CharField(max_length=5, default='FCR')

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.course, self.type)


class UserTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(learnModule.models.Course, on_delete=models.CASCADE)
    percentCompleted = models.CharField(max_length=6)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.course, self.percentCompleted)


class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logInTime = models.DateTimeField('time login', blank=True, null=True)
    logOutTime = models.DateTimeField('time logout', blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s %s %s' % (self.user, self.logInTime, self.logOutTime)


class UserSharedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(learnModule.models.Content, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return '%s %s' % (self.user, self.content)
