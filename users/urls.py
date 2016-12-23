from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_create/$', views.signup_create, name='signup_create'),
    url(r'^Login/$', views.login_user, name='login_user'),
    url(r'^Logout/$', views.logout_user),
    url(r'^EditProfile/$', views.edit_profile, name='edit_profile'),
    url(r'^Profile/$', views.profile_detail, name='profile_detail'),
    url(r'^profileDetail/$', views.profile_detail, name='profile_detail'),
]



