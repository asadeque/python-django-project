from django.contrib import admin
from .models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)


class WrittenForAdmin(admin.ModelAdmin):
    class Meta:
        model = WrittenFor

admin.site.register(WrittenFor, WrittenForAdmin)


class InformationForAdmin(admin.ModelAdmin):
    class Meta:
        model = InformationFor

admin.site.register(InformationFor, InformationForAdmin)


class WrittenByAdmin(admin.ModelAdmin):
    class Meta:
        model = WrittenBy

admin.site.register(WrittenBy, WrittenByAdmin)


class FormatAdmin(admin.ModelAdmin):
    class Meta:
        model = Format

admin.site.register(Format, FormatAdmin)


class CopyRightAdmin(admin.ModelAdmin):
    class Meta:
        model = CopyRight

admin.site.register(CopyRight, CopyRightAdmin)


class SourceAdmin(admin.ModelAdmin):
    class Meta:
        model = Source

admin.site.register(Source, SourceAdmin)


class ResourceTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = ResourceType

admin.site.register(ResourceType, ResourceTypeAdmin)


class LibraryTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = LibraryType

admin.site.register(LibraryType, LibraryTypeAdmin)


class LibraryAdmin(admin.ModelAdmin):
    class Meta:
        model = Library

admin.site.register(Library, LibraryAdmin)






