from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/$', views.help, name='help'),
    url(r'^team/$', views.team, name='team'),
    url(r'^users/', include('users.urls')),
    url(r'^language/(\d+)/$', views.language, name='language'),
    url(r'^Learned/(?P<pk>\w+)/$', views.learned_user),
    url(r'^DelLearnedContent/(?P<pk>\w+)/$', views.delete_content_user),
    url(r'^Favourite/(?P<pk>\w+)/$', views.favourite_content_user),
    url(r'^DelFavourite/(?P<pk>\w+)/$', views.delete_favourite_content_user),
    url(r'^UnFavourite/(?P<pk>\w+)/$', views.delete_content_user),
    url(r'^FavouriteCourse/(?P<pk>\w+)/$', views.favourite_course_user),
    url(r'^DelFavouriteCourse/(?P<pk>\w+)/$', views.delete_favourite_course_user),
    url(r'^FPIC/$', views.FPIC, name='FPIC'),
    url(r'^Consultation/$', views.Consultation, name='Consultation'),
    url(r'^FPICCourses/$', views.FPICCourses, name='FPICCourses'),
    url(r'^ConsultCourses/$', views.ConsultCourses, name='ConsultCourses'),
    url(r'^CourseHome/(?P<pk>\w+)/$', views.courseHome, name='courseHome'),
    url(r'^contentsHome/(?P<pk>\w+)/$', views.contentsHome, name='contentsHome'),
    url(r'^quiz/(?P<pk>\w+)/$', views.quiz_save, name='quiz_save'),
    url(r'^quizResult/$', views.quiz_result, name='quiz_result'),
    url(r'^checklist/$', views.checklist_save, name='checklist_save'),
    url(r'^checkListAns/$', views.checkListAns, name='checkListAns'),
    url(r'^boolQuiz/(?P<pk>\w+)/$', views.boolQuiz_save, name='boolQuiz_save'),
    url(r'^boolQuizResult/$', views.boolQuiz_result, name='boolQuiz_result'),
    url(r'^images/(?P<filename>[^~,]+)/(?P<pk>\w+)/$', views.pdfDownload),
    url(r'^CourseHome/(?P<pk>\w+)/(?P<content_id>\w+)/$', views.courseHome, name='courseHome'),
    url(r'^contentHome/(?P<pk>\w+)/$', views.contentHome, name='contentHome'),
]
