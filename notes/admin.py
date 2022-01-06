from django.contrib import admin
from notes.models import Note

from .models import (
    Note
)


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Note, NoteAdmin)

# Register your models here.
