from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class NoteType:
    VIDEO = "video"
    AUDIO = "audio"
    PDF = "pdf"
    TEXT = "text"

    CHOICES = [
        (VIDEO, "Video"),
        (AUDIO, "Audio"),
        (PDF, "PDF"),
        (TEXT, "Text"),
    ]

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    type = models.CharField(_("Type"), max_length=10, choices=NoteType.CHOICES, default=NoteType.TEXT)
    file = models.FileField(upload_to='notes/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    # Erollment or course linking to the note

    class Meta:
        """Meta definition for Note"""

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    def __str__(self):
        """Unicode representation of Note"""
        return self.title

