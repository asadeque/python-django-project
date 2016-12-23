from django.contrib import admin

# Register your models here.
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "createdDate", "author"]
    list_display_links = ["createdDate"]
    list_filter = ["title", "createdDate", "updatedDate"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["blog", "name", "email", "website", "createdDate"]
    list_display_links = ["createdDate"]
    list_filter = ["blog", "createdDate"]
    search_fields = ["text", "name"]
    list_editable = ["name"]
    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)


class UserFavouriteBlogAdmin(admin.ModelAdmin):
    class Meta:
        model = UserFavouriteBlog

admin.site.register(UserFavouriteBlog, UserFavouriteBlogAdmin)
