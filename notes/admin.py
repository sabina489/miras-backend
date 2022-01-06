from django.contrib import admin
from notes.models import Note

from .models import (
    Note
)


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'title', 'type', 'created_at',
                    'price', 'free', 'courses')
    list_filter = ('type', 'price', 'courses')


admin.site.register(Note, NoteAdmin)
