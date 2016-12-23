from django.contrib import admin

# Register your models here.
from .models import *

class StoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Story

admin.site.register(Story, StoryAdmin)


class StoryChildAdmin(admin.ModelAdmin):
    class Meta:
        model =StoryChild

admin.site.register(StoryChild, StoryChildAdmin)
