from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
# Create your models here.


User = get_user_model()


class CourseCategory(models.Model):
    """Model definition for CourseCategory."""

    name = models.CharField(_("name"), max_length=100)
    # Apply parent child trick.
    # This avoids the necessity to create numerous sparse tables
    # for every new category admin thinks of. Instead a single table
    # can have multiple many to one relationship within itself
    # to signify subcategories.

    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    class Meta:
        """Meta definition for CourseCategory."""

        verbose_name = 'CourseCategory'
        verbose_name_plural = 'CourseCategorys'

    def __str__(self):
        """Unicode representation of CourseCategory."""
        return self.name


class CourseStatus:
    INSESSION = "insession"  # course has active classes currently
    UPCOMING = "upcoming"  # course is being planned
    ENDED = "ended"  # course has successfully ended
    CANCELLED = "cancelled"  # course has been abruptly ended

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
        "category"), related_name="courses", on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, verbose_name=_(
        "instructor"), related_name="courses", on_delete=models.CASCADE)
    link = models.URLField(_("link"), max_length=200)
    password = models.CharField(_("password"), max_length=128, help_text=_(
        "Use'[algo]$[salt]$[hexdigest]' or use the < a href=\"password/\">change password form</a>."))
    status = models.CharField(
        _("status"), max_length=32, default=CourseStatus.UPCOMING)

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of Course."""
        return self.name
