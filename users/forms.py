from django import forms
from django.forms import ModelForm

from users.models import User
from django.db import models

LANGUAGE_CHOICES = (
    ('EN', 'En.'),
    ('SP', 'Sp.'),
    ('FR', 'Fr.'),
)


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        # fields = ("title", "body", "pub_date")
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        fields = '__all__'
        email = forms.EmailField(min_length=1, max_length=100)
        # exclude = ['password',]
        # fields=['book_id','book_name','author_name','publisher_name']

class EditUserForm(forms.ModelForm):
    image = forms.ImageField(label='Change your profile picture ')
    firstName = forms.CharField(label='First and Last Names ', max_length=200)
    password = forms.CharField(required = False, label='Password ', max_length=256, widget=forms.PasswordInput)
    email = forms.EmailField(required = True, label='Email ', min_length=1, max_length=100)
    profileHighlight = forms.CharField(required = False, label='Share a little bit of who you are ')
    class Meta:
        model = User
        exclude = ['lastName','userName', 'userType']


