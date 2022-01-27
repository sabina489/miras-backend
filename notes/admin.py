from django.contrib import admin
from django.forms import ModelForm, TextInput, models
from notes.models import Note

from .models import (
    Note
)

from content.admin import ContentInline


class NoteAdminForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'body': admin.widgets.AdminTextareaWidget(attrs={"rows": 2, "cols": 1})
        }


class NoteInline(admin.TabularInline):
    model = Note
    form = NoteAdminForm
    extra = 1
    readonly_fields = ('created_by',)
    show_change_link = True


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_by',)
    list_display = ('title', 'type', 'created_at',
                    'price', 'free', 'courses', 'part')
    list_filter = ('type', 'price', 'courses', 'part')
    inlines = [ContentInline, ]

    def save_model(self, request, obj, form, change):
        if not change:
            if not hasattr(obj, 'created_by'):
                obj.created_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if not hasattr(instance, 'created_by'):
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(Note, NoteAdmin)
