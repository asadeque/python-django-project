from django import forms
from django.forms import ModelForm

from learnModule.models import Course, Content, Topic
from story.models import Story
from django.db import models

LANGUAGE_CHOICES = (
    ('EN', 'En.'),
    ('SP', 'Sp.'),
    ('FR', 'Fr.'),
)


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        # fields = ("title", "body", "pub_date")
        fields = '__all__'

