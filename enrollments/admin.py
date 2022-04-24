from django.contrib import admin
from enrollments.models import (
    Enrollment,
    ExamStatus,
)

from exams.models import (
    QuestionStatus
)
from payments.admin import OnlinePaymentInline, BankPaymentInline


class QuestionStatusInline(admin.StackedInline):
    model = QuestionStatus


class ExamStatusInline(admin.TabularInline):
    model = Enrollment.exams.through
    readonly_fields = ('id', 'score',)
    extra = 1


class EnrollmentAdmin(admin.ModelAdmin):

    def enrolled_on(self, obj):
        enrolled = ""
        if obj.parts:
            enrolled += ", ".join([f"{p.name}(part)" for p in obj.parts.all()])
        if obj.exams:
            enrolled += "(exams), ".join(
                [f"{e.name}(exam)" for e in obj.exams.all()])
        if obj.notes:
            enrolled += "(notes), ".join(
                [f"{n.title}(note)" for n in obj.notes.all()])
        return enrolled
    
    def email(self, obj):
        return obj.student.email

    readonly_fields = ('id',)
    list_display = ('id', 'student',"email", 'status', 'enrolled_on', 'created_at')
    list_filter = ('status',"parts__course", 'parts', 'exams', 'notes')
    search_fields = ['student__phone',]
    inlines = [
        ExamStatusInline,
        OnlinePaymentInline,
        BankPaymentInline,
    ]
    exclude = ('exams',)


class ExamStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'enrollment', 'exam', 'score',)
    list_filter = ('exam',)
    inlines = [
        QuestionStatusInline,
    ]


# Register your models here.
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(ExamStatus, ExamStatusAdmin)
