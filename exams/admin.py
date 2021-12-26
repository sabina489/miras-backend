from django.contrib import admin

import nested_admin

from .models import (
    Exam,
    Question,
    QuestionStatus,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    Option,
)

# Register your models here.

class OptionsInLine(nested_admin.NestedStackedInline):
    model = Option
    extra = 1

class QuestionInLine(nested_admin.NestedStackedInline):
    model = Question
    inlines = [
        OptionsInLine,
    ]
class ExamAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
class ExamCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    inlines = [
        OptionsInLine,
    ]
class QuestionStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
class MockExamAdmin(nested_admin.NestedModelAdmin):
    readonly_fields = ('id', )
    inlines = [
        QuestionInLine,
    ]
class MCQExamAdmin(nested_admin.NestedModelAdmin):
    readonly_fields = ('id', )
    inlines = [
        QuestionInLine,
    ]
class GorkhapatraExamAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
class OptionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStatus, QuestionStatusAdmin)
admin.site.register(MockExam, MockExamAdmin)
admin.site.register(MCQExam, MCQExamAdmin)
admin.site.register(GorkhapatraExam, GorkhapatraExamAdmin)
admin.site.register(Option, OptionAdmin)
