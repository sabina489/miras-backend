from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from courses.models import Course
from courses.validators import validate_positive
from part.models import Part

User = get_user_model()


class NoteType:
    RECORDED_VIDEO = "Recorded Video"
    OTHERS = "Others"

    CHOICES = [
        (RECORDED_VIDEO, "Recorded Video"),
        (OTHERS, "Others"),
    ]


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    type = models.CharField(_("Type"), max_length=20,
                            choices=NoteType.CHOICES, default=NoteType.RECORDED_VIDEO)
    # file = models.FileField(upload_to='notes/files/', blank=True, null=True)
    free = models.BooleanField(default=False)
    price = models.FloatField(_("price"), default=0.0,
                              validators=[validate_positive])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')

    courses = models.ForeignKey(Course, verbose_name=_(
        "courses"), on_delete=models.CASCADE, related_name='notes')
    part = models.ForeignKey(
        Part, on_delete=models.CASCADE, related_name='notes', blank=True, null=True)
    # Erollment or course or part linking to the note

    class Meta:
        """Meta definition for Note"""

        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at']

    def __str__(self):
        """Unicode representation of Note"""
        return self.title
