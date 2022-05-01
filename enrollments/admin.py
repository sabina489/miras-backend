from django.contrib import admin
from django.shortcuts import render
from enrollments.forms import EmailForm
from enrollments.models import (
    Enrollment,
    ExamStatus,
)

from exams.models import (
    QuestionStatus
)
from payments.admin import OnlinePaymentInline, BankPaymentInline
from import_export.admin import ExportMixin
from enrollments.resources import EnrollmentResource
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from common.utils import send_mail_common
from django.template.response import TemplateResponse


class QuestionStatusInline(admin.StackedInline):
    model = QuestionStatus


class ExamStatusInline(admin.TabularInline):
    model = Enrollment.exams.through
    readonly_fields = ('id', 'score',)
    extra = 1


class EnrollmentAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EnrollmentResource

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

    def name(self, obj):
        return obj.student.get_full_name()

    def send_email(self, request, queryset):
        opts = self.model._meta
        app_label = opts.app_label
        context = {
            **self.admin_site.each_context(request),
            'title': "Send Email",
            'subtitle': None,
            'object_name': "Enrollment",
            'object': queryset,
            'model_count': queryset.count(),
            'opts': opts,
            'app_label': app_label,
            'preserved_filters': self.get_preserved_filters(request),
            'items': queryset,
        }
        if 'apply' in request.POST:  # if user pressed 'apply' on intermediate page
            # Cool thing is that params will have the same names as in forms.py
            email_context = {
                "message": request.POST["message"],
            }
            subject = request.POST["subject"]

            # Run background task that will send broadcast messages
            for enroll in queryset:
                if to := enroll.student.email:
                    send_mail_common("admin/send_mail.html",
                                     email_context, [to], subject)

            # Show alert that everything is cool
            self.message_user(
                request, f"Message has been send to {queryset.count()} students")

            # Return to previous page
            return HttpResponseRedirect(request.get_full_path())

        # Create form and pass the data which objects were selected before triggering 'broadcast' action
        # We create an intermediate page right here
        form = EmailForm(
            initial={'_selected_action': queryset.values_list('id', flat=True)})
        context['form'] = form

        # We need to create a template of intermediate page with form - but this is really easy
        return TemplateResponse(request, "admin/email_data.html", context)

    readonly_fields = ('id',)
    list_display = ('id', 'name', 'student', "email",
                    'status', 'enrolled_on', 'created_at')
    list_filter = ('status', "parts__course", 'parts', 'exams', 'notes')
    search_fields = ['student__phone', ]
    inlines = [
        ExamStatusInline,
        OnlinePaymentInline,
        BankPaymentInline,
    ]
    actions = ['send_email']
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
