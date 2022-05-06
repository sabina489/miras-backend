from django import forms
from django.contrib import admin

import nested_admin

from file_resubmit.admin import AdminResubmitMixin

from .models import (
    Exam,
    Question,
    QuestionStatus,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    Option,
    Officer,
)


class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class CustomStackedInline(nested_admin.NestedStackedInline):
    template = "inlines/stacked.html"


class CustomTabularInline(nested_admin.NestedTabularInline):
    template = "inlines/tabular.html"


class OptionsAdminForm(forms.ModelForm):
    class Meta:
        model = Option
        # fields = "__all__"
        exclude = ("marks", "feedback",)
        widgets = {
            "detail": admin.widgets.AdminTextareaWidget(attrs={"rows": 2, "cols": 1, 'class': 'vTextField'}),
        }


class OptionsInLine(AdminResubmitMixin, nested_admin.NestedTabularInline):
    model = Option
    extra = 4
    max_num = 6
    form = OptionsAdminForm


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
            "detail": admin.widgets.AdminTextareaWidget(attrs={"rows": 3, "cols": 2}),
        }


class QuestionInLine(AdminResubmitMixin, CustomStackedInline):
    model = Question
    inlines = [
        OptionsInLine,
    ]
    form = QuestionAdminForm


class ExamCommonAdmin(admin.ModelAdmin):

    def category_list(self, obj):
        return ", ".join([q.name for q in obj.category.all()])

    list_display = ('id', 'name', 'category_list',
                    'course',  'price', 'created_at',)
    list_filter = ("course", "category")
    autocomplete_fields = ("category", )
    readonly_fields = ('id', 'created_at')


class ExamAdmin(ExamCommonAdmin):
    list_filter = ExamCommonAdmin.list_filter + ("kind",)
    list_display = ExamCommonAdmin.list_display + ("kind",)


class MockExamAdmin(ExamCommonAdmin, nested_admin.NestedModelAdmin):
    list_display = ExamCommonAdmin.list_display + ('timer',)
    inlines = [
        QuestionInLine,
    ]
    autocomplete_fields = ExamCommonAdmin.autocomplete_fields + ("officer",)


class MCQExamAdmin(ExamCommonAdmin, nested_admin.NestedModelAdmin):
    inlines = [
        QuestionInLine,
    ]


class GorkhapatraExamAdmin(ExamCommonAdmin):
    list_display = ExamCommonAdmin.list_display + ('content',)


class QuestionAdmin(AdminResubmitMixin, admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('id', 'detail', 'exam',  'marks',)
    list_filter = ('exam', )
    inlines = [
        OptionsInLine,
    ]


class QuestionStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'updated_at')
    list_display = ('id', 'exam_stat', 'question',
                    'selected_option', 'updated_at',)
    list_filter = ('question',)


class OptionAdmin(AdminResubmitMixin, admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('id', 'question', 'detail', 'correct', 'marks',)
    list_filter = ('question',)


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStatus, QuestionStatusAdmin)
admin.site.register(MockExam, MockExamAdmin)
admin.site.register(MCQExam, MCQExamAdmin)
admin.site.register(GorkhapatraExam, GorkhapatraExamAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Officer, OfficerAdmin)
