from django.contrib import admin

from courses.models import (
    Course,
    CourseCategory,
    CourseRequest,
)
from notes.admin import NoteInline


class CourseAdmin(admin.ModelAdmin):

    def date_time(self, obj):
        return f"{obj.start_date} - {obj.end_date}"

    readonly_fields = ('id',)
    list_display = ('id', 'name', 'category', 'instructor',
                    'status', 'price', 'date_time')
    list_filter = ('status', 'category')
    inlines = [NoteInline, ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not hasattr(instance, 'created_by'):
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()

    readonly_fields = ('parts',)

    @admin.display
    def parts(self, instance):
        return (',').join(part.name for part in instance.parts.all())


class CourseCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'parent')
    list_filter = ('parent',)
    search_fields = ["name"]


class CourseRequestAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'course_name', 'course_category', 'requester_name', 'requester_phone', 'status','created_at')
    list_filter = ('status',)


admin.site.register(CourseRequest, CourseRequestAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)
