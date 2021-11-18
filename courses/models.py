from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
# Create your models here.


User = get_user_model()


class CourseCategory(models.Model):
    """Model definition for CourseCategory."""

    name = models.CharField(_("name"), max_length=100)

    class Meta:
        """Meta definition for CourseCategory."""

        verbose_name = 'CourseCategory'
        verbose_name_plural = 'CourseCategorys'

    def __str__(self):
        """Unicode representation of CourseCategory."""
        pass


class CourseStatus:
    INSESSION = "insession" # course has active classes currently
    UPCOMING = "upcoming" # course is being planned
    ENDED = "ended" # course has successfully ended
    CANCELLED = "cancelled" # course has been abruptly ended

    CHOICES = [
        (INSESSION, "insession"),
        (UPCOMING, "upcoming"),
        (ENDED, "ended"),
        (CANCELLED, "cancelled")
    ]

class Course(models.Model):
    """Model definition for Course."""

    name = models.CharField(_("name"), max_length=200)
    category = models.ForeignKey(CourseCategory, verbose_name=_(
        "category"), on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, verbose_name=_(
        "instructor"), on_delete=models.CASCADE)
    link = models.URLField(_("link"), max_length=200)
    password = models.CharField(_("password"), max_length=128, help_text=_(
        "Use'[algo]$[salt]$[hexdigest]' or use the < a href=\"password/\">change password form</a>."))
    status = models.CharField(_("status"), max_length=32, default=CourseStatus.UPCOMING)

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of Course."""
        pass
