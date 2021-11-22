from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
User = get_user_model()


class EnrollmentStatus:
    ACTIVE = "active"  # student can access all the enrolled objects
    INACTIVE = "inactive"  # enrollment/access has expired
    PENDING = "pending"  # enrollment is awaiting admin verification
    CANCELLED = "cancelled"  # enrollment is abruply expired
    CHOICES = [
        (ACTIVE, "active")
        (INACTIVE, "inactive")
        (PENDING, "pending")
        (CANCELLED, "cancelled")
    ]


class Enrollment(models.Model):
    """Model definition for Enrollment."""
    user = models.ForeignKey(User, verbose_name=_(
        "student"), related_name="enrollments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        _("status"), max_length=32, choices=EnrollmentStatus, 
        default=EnrollmentStatus.PENDING)
    # TODO: Add one to one field to payment

    class Meta:
        """Meta definition for Enrollment."""

        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'

    def __str__(self):
        """Unicode representation of Enrollment."""
        return "{} at {}".format(self.user.__str__, self.created_at)
