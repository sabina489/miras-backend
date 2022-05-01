from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from courses.models import Course
from notes.models import Note
from part.models import Part

User = get_user_model()


def content_location(instance, filename):
    return 'content/{0}/{1}'.format(instance.note.id, filename)


class ContentType:
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


class Content(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(_("Type"), max_length=10,
                            choices=ContentType.CHOICES, default=ContentType.VIDEO)
    file = models.FileField(upload_to=content_location, blank=True, null=True)
    note = models.ForeignKey(
        Note, on_delete=models.CASCADE, related_name="contents", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='contents')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


def recorded_content_location(instance, filename):
    return 'content/{0}/{1}'.format(instance.part.id, filename)


class RecordedVideo(models.Model):
    name = models.CharField(max_length=200, default="Recorded Video")
    file = models.FileField(upload_to=recorded_content_location)
    part = models.ForeignKey(
        Part, on_delete=models.CASCADE, related_name='recorded_video')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recorded_video')

    def __str__(self) -> str:
        return f"{self.name} - {self.part.name}"
