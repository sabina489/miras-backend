import uuid

from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

from gateways.register import gateway_factory
# from enrollments.models import Enrollment


class PaymentStatus:
    UNPAID = "unpaid"  # Aswaiting payment
    INPROGRESS = "inprogress"  # verification in progress
    PAID = "paid"  # payment success
    ERROR = "error"  # verification error
    CHOICES = [
        (UNPAID, "unpaid"),
        (INPROGRESS, "inprogress"),
        (PAID, "paid"),
        (ERROR, "error"),
    ]

# Create your models here.


class Payment(models.Model):
    """Model definition for Payment."""

    # TODO: Define fields here
    # does amount need to be positive number only
    amount = models.DecimalField(
        _("amount"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    # generate a unique id field
    # pid = models.UUIDField(_("pid"), primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey("enrollments.Enrollment", verbose_name=_("enrollment"),
                                   related_name=_("payments") on_delete=models.CASCADE)
    status = models.CharField(_("status"), max_length=32,
                              choices=PaymentStatus.CHOICES, default=PaymentStatus.UNPAID)

    def change_status(self, new_status):
        self.status = new_status

    class Meta:
        """Meta definition for Payment."""

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        """Unicode representation of Payment."""
        pass


class OnlinePayment(Payment):
    """Model for online based payment."""
    variant = models.CharField(_("variant"), max_length=32)
    tax_amount = models.DecimalField(
        _("tax_amount"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    service_charge = models.DecimalField(
        _("service_charge"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    delivery_charge = models.DecimalField(
        _("delivery_charge"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    merchant_code = models.CharField(_("scd"), max_length=32)
    transation_code = models.CharField(_("txcode"), max_length=128)
    # this is the field to store extra content that may be present only
    # for one of the gateway
    extra_content = models.JSONField(default=dict)

    class Meta:
        """Meta definition for esewa based payment."""
        verbose_name = 'OnlinePayment'
        verbose_name_plural = 'OnlinePayments'

    def capture(self, amount=None):
        gateway = gateway_factory.get_gateway(self.variant)
        status = gateway.capture(self, amount)
        self.change_status(status)



class BankPayment(Payment):
    """Model for bank based pay"""
    voucher = models.ImageField(_("voucher"), upload_to=None, blank=True, null=True)
    class Meta:
        "Meta definition for bank based payment."
        verbose_name = 'BankPayment'
        verbose_name_plural = 'BankPayments'