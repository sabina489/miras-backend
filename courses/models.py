from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

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
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CourseCategory, verbose_name=_(
        "category"), related_name="courses", on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, verbose_name=_(
        "instructor"), related_name="courses", on_delete=models.CASCADE)
    link = models.URLField(_("link"), max_length=200)
    password = models.CharField(_("password"), max_length=128, help_text=_(
        "Use'[algo]$[salt]$[hexdigest]' or use the < a href=\"password/\">change password form</a>."))
    status = models.CharField(
        _("status"), max_length=32, choices=CourseStatus.CHOICES,
        default=CourseStatus.UPCOMING)
    detail = models.TextField(_("detail"), null=True, blank=True)
    detail1 = models.TextField(_("detail1"), null=True, blank=True)
    video = models.URLField(_("video"), max_length=200, null=True, blank=True)
    price = models.FloatField(_("price"), default=0.0)
    start_date = models.DateField(_("start"), null=True, blank=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("end"), null=True, blank=True, auto_now=False, auto_now_add=False)


    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['created_at']

    def __str__(self):
        """Unicode representation of Course."""
        return self.name


class CourseRequestStatus:
    APPROVED = "Approved"
    REQUEST = "Request"
    DENIED = "Denied"

    CHOICES = [
        (APPROVED, "Approved"),
        (REQUEST, "Request"),
        (DENIED, "Denied")
    ]


class CourseRequest(models.Model):
    """Model definition for CourseRequest."""

    course_name = models.CharField(_("Course Name"), max_length=200)
    course_category = models.CharField(_("Course Category"), max_length=200)
    requester_name = models.CharField(_("Requester Name"), max_length=200)
    requester_email = models.EmailField(_("Requester Email"))
    requester_phone = RegexValidator(
        regex=r'^9\d{9}', message="Enter a valid phonenumber 9XXXXXXXXX")
    status = models.CharField(choices=CourseRequestStatus.CHOICES,
                              default=CourseRequestStatus.REQUEST, max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        """Unicode representation of CourseRequest."""
        return self.course_name
