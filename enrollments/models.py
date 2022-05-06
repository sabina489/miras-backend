from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from decimal import Decimal


from part.models import Part
# Create your models here.
User = get_user_model()


class EnrollmentStatus:
    ACTIVE = "active"  # student can access all the enrolled objects
    INACTIVE = "inactive"  # enrollment/access has expired
    PENDING = "pending"  # enrollment is awaiting admin verification
    CANCELLED = "cancelled"  # enrollment is abruply expired
    CHOICES = [
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (PENDING, "pending"),
        (CANCELLED, "cancelled")
    ]

# TODO: make this
# class EnrolledObjectStatus(models.Model):

#     class Meta:
#         abstract = True
# class EnrolledPartStatus(EnrolledObjectStatus):


class Enrollment(models.Model):
    """Model definition for Enrollment."""
    student = models.ForeignKey(User, verbose_name=_(
        "student"), related_name="enrollments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        _("status"), max_length=32, choices=EnrollmentStatus.CHOICES,
        default=EnrollmentStatus.PENDING)
    parts = models.ManyToManyField(Part, verbose_name=_(
        "parts"), related_name="enrolls", blank=True)
    exams = models.ManyToManyField("exams.Exam", verbose_name=_("exams"),
                                   related_name="enrolls", blank=True, through="ExamStatus")
    notes = models.ManyToManyField("notes.Note", verbose_name=_("notes"),
                                   related_name="enrolls", blank=True)

    class Meta:
        """Meta definition for Enrollment."""

        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        """Unicode representation of Enrollment."""
        # TODO: make this more readable for admin panel
        return "{} at {}".format(self.student.__str__(), self.created_at)
# TODO: part status
# TODO: notes status


class ExamStatus(models.Model):
    """Model definition for ExamStatus."""
    enrollment = models.ForeignKey(Enrollment, verbose_name=_(
        "enrollment"), related_name="exam_states", on_delete=models.CASCADE)
    exam = models.ForeignKey("exams.Exam", verbose_name=_(
        "exam"), related_name="exam_states", on_delete=models.CASCADE)
    score = models.DecimalField(
        _("score"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    submitted = models.BooleanField(_("submitted"), default=False)

    class Meta:
        """Meta definition for ExamStatus."""

        verbose_name = 'ExamStatus'
        verbose_name_plural = 'ExamStatuss'

    def __str__(self):
        """Unicode representation of ExamStatus."""
        return "enrollment {} for exam {}".format(
            self.enrollment,
            self.exam
        )
