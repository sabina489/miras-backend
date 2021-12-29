from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Note, NoteAdmin)
