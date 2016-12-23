from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.story_list, name='story_list'),
    url(r'^StoryList/$', views.story_list, name='story_list'),
    url(r'^StoryDetail/(?P<pk>\w+)/$', views.story_detail, name='story_detail'),
]
