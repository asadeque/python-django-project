from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^list/$', views.blog_list, name='list'),
    url(r'^create/$', views.blog_create),
    url(r'^detail/(?P<id>\d+)/$', views.blog_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.blog_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.blog_delete),
    url(r'^FavouriteBlog/(?P<pk>\w+)/$', views.favourite_blog_user),
    url(r'^DelFavouriteBlog/(?P<pk>\w+)/$', views.delete_favourite_blog_user),
]



