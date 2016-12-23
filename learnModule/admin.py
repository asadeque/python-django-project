from django.contrib import admin

# Register your models here.
from .models import *

class LanguageAdmin(admin.ModelAdmin):
    class Meta:
        model = Language

admin.site.register(Language, LanguageAdmin)


class SubMenuLangAdmin(admin.ModelAdmin):
    class Meta:
        model = SubMenuLang

admin.site.register(SubMenuLang, SubMenuLangAdmin)


class ComplexityAdmin(admin.ModelAdmin):
    class Meta:
        model = Complexity

admin.site.register(Complexity, ComplexityAdmin)


class TopicAdmin(admin.ModelAdmin):
    class Meta:
        model = Topic

admin.site.register(Topic, TopicAdmin)


class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course

admin.site.register(Course, CourseAdmin)


class ContentStyleAdmin(admin.ModelAdmin):
    class Meta:
        model = ContentStyle

admin.site.register(ContentStyle, ContentStyleAdmin)


class ContentAdmin(admin.ModelAdmin):
    class Meta:
        model = Content

admin.site.register(Content, ContentAdmin)


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Choice

admin.site.register(Choice, ChoiceAdmin)


class QuizAdmin(admin.ModelAdmin):
    class Meta:
        model = Quiz

admin.site.register(Quiz, QuizAdmin)


class CheckListAdmin(admin.ModelAdmin):
    class Meta:
        model = CheckList

admin.site.register(CheckList, CheckListAdmin)


class SummaryAdmin(admin.ModelAdmin):
    class Meta:
        model = Summary

admin.site.register(Summary, SummaryAdmin)


class SummaryChildAdmin(admin.ModelAdmin):
    class Meta:
        model = SummaryChild

admin.site.register(SummaryChild, SummaryChildAdmin)


class FinishAdmin(admin.ModelAdmin):
    class Meta:
        model = Finish

admin.site.register(Finish, FinishAdmin)
