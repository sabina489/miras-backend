from django.db import models
from django.db.models.fields.related import ForeignKey
from decimal import Decimal

from courses.models import Course
from courses.validators import validate_positive
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Part(models.Model):
    """Model definition for Part."""

    name = models.CharField(_("name"), max_length=100)
    course = models.ForeignKey(Course, verbose_name=_("course"),
                               related_name="parts", on_delete=models.CASCADE)
    # enrolls = models.ManyToManyField(Enrollment, verbose_name=_(
    #     "enrolls"), related_name="parts", blank=True)
    detail = models.TextField(_("detail"), null=True, blank=True)
    price = models.DecimalField(_("price"), max_digits=7, decimal_places=2, default=Decimal("0.0"),
                                validators=[validate_positive])

    class Meta:
        """Meta definition for Part."""

        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        """Unicode representation of Part."""
        return self.name
