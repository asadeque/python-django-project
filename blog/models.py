from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
import users



# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='staticfiles/blog/images', null=True, blank=True,
            width_field='width_field',
            height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(users.models.User)
    n_comments = models.IntegerField(null=True, blank=True)
    n_pingbacks = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/blog/detail/%s/" %(self.id)
        return reverse("blog:detail", kwargs={"id":self.id})

    class Meta:
        ordering = ["-createdDate", "-updatedDate"]


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-createdDate", "-updatedDate"]

    def get_absolute_url(self):
            return reverse("blog:detail", kwargs={"id":self.id})


class UserFavouriteBlog(models.Model):
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedDate = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return '%s %s' % (self.user, self.blog)
