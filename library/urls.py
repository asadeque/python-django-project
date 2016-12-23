from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.library, name='library'),
    url(r'^library/$', views.library, name='library'),
    url(r'^libraryDetails/(?P<pk>\w+)/$', views.libraryDetails, name='libraryDetails'),
    url(r'^Favourite/(?P<pk>\w+)/$', views.favourite_resource_user),
    url(r'^DelFavourite/(?P<pk>\w+)/$', views.delete_favourite_resource_user),
    url(r'^UnFavourite/(?P<pk>\w+)/$', views.delete_resource_user),
    url(r'^pdf/(?P<filename>[^~,]+)/(?P<pk>\w+)/$', views.pdfDownload),
    url(r'^DelDownloadedResource/(?P<pk>\w+)/$', views.delete_downloaded_resource_user),
    url(r'^language/(\d+)/$', views.language, name='language'),
]
