from django.contrib import admin
from enrollments.models import (
    Enrollment,
    ExamStatus,
)

from exams.models import (
    QuestionStatus
)


class QuestionStatusInline(admin.StackedInline):
    model = QuestionStatus

class ExamStatusInline(admin.TabularInline):
    model = Enrollment.exams.through
    readonly_fields = ('id', 'score',)
    extra = 1
class EnrollmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [
        ExamStatusInline,
    ]
    exclude = ('exams',)


class ExamStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [
        QuestionStatusInline,
    ]


# Register your models here.
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(ExamStatus, ExamStatusAdmin)
