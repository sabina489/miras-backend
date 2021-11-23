from django.db import models
from django.db.models.fields.related import ForeignKey

from enrollments.models import Enrollment
from courses.models

# Create your models here.


class Part(models.Model):
    """Model definition for Part."""

    name = models.CharField(_("name"), max_length=100)
    course = models.ForeignKey("courses.Course", verbose_name=_("course"),
                               related_name="parts", on_delete=models.CASCADE)
    enrolls = models.ManyToManyField(Enrollment, verbose_name=_(
        "enrolls"), related_name="parts", on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField(_("detail"), null=True, blank=True)
    price = models.FloatField(_("price"), default=0.0)
    # TODO: Add field for count
    # TODO: Count the number enrollment to parts

    class Meta:
        """Meta definition for Part."""

        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        """Unicode representation of Part."""
        return self.name
