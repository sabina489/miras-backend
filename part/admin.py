from django.contrib import admin

from part.models import (
    Part,
)
from notes.admin import NoteInline


class PartAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'course', 'price', 'detail',)
    list_filter = ('course',)
    inlines = [NoteInline, ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not hasattr(instance, 'created_by'):
                instance.created_by = request.user
            instance.courses = form.instance.course
            instance.save()
        formset.save_m2m()


admin.site.register(Part, PartAdmin)
