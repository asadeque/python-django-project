"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    url(r'^users/', include('users.urls')),

    """
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', 'homepage.views.home'),
    # url(r'^$', 'learnModules.views.home', name='home'),
    url(r'^$', include('learnModule.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^learnModule/', include('learnModule.urls')), # , namespace='learnModule'
    url(r'^users/', include('users.urls', namespace='users')),
    # url(r'^blog/$', "blog.views.blog_home"),
    # url(r'^blog/$', views.blog_home, name='blog_home'),
    # url(r'^blog/$', "<app_name>.views.<function_name>"),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^story/', include('story.urls', namespace='story')),
    url(r'^library/', include('library.urls', namespace='library')),
    ]

# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
