from django.contrib import admin
from .models import *



class UserTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = UserType

admin.site.register(UserType, UserTypeAdmin)


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    class Meta:
        model = UserCourse

admin.site.register(UserCourse, UserCourseAdmin)


class UserTopicAdmin(admin.ModelAdmin):
    class Meta:
        model = UserTopic

admin.site.register(UserTopic, UserTopicAdmin)


class UserContentAdmin(admin.ModelAdmin):
    class Meta:
        model = UserContent

admin.site.register(UserContent, UserContentAdmin)


class UserQuizAdmin(admin.ModelAdmin):
    class Meta:
        model = UserQuiz

admin.site.register(UserQuiz, UserQuizAdmin)


class UserChecklistAdmin(admin.ModelAdmin):
    class Meta:
        model = UserChecklist

admin.site.register(UserChecklist, UserChecklistAdmin)


class UserFavouriteContentAdmin(admin.ModelAdmin):
    class Meta:
        model = UserFavouriteContent

admin.site.register(UserFavouriteContent, UserFavouriteContentAdmin)

class UserFavouriteCourseAdmin(admin.ModelAdmin):
    class Meta:
        model = UserFavouriteCourse

admin.site.register(UserFavouriteCourse, UserFavouriteCourseAdmin)

class UserTrackAdmin(admin.ModelAdmin):
    class Meta:
        model = UserTrack

admin.site.register(UserTrack, UserTrackAdmin)


class UserLogAdmin(admin.ModelAdmin):
    class Meta:
        model = UserLog

admin.site.register(UserLog, UserLogAdmin)


class UserSharedContentAdmin(admin.ModelAdmin):
    class Meta:
        model = UserSharedContent

admin.site.register(UserSharedContent, UserSharedContentAdmin)


class UserResourceDownloadAdmin(admin.ModelAdmin):
    class Meta:
        model = UserResourceDownload

admin.site.register(UserResourceDownload, UserResourceDownloadAdmin)


class UserFavouriteResourceAdmin(admin.ModelAdmin):
    class Meta:
        model = UserFavouriteResource

admin.site.register(UserFavouriteResource, UserFavouriteResourceAdmin)
