import uuid

from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _

from .gateways.register import gateway_factory
# from enrollments.models import Enrollment


from . import PaymentStatus
# Create your models here.

class OnlinePaymentVariants():
    keys = gateway_factory.get_gateways()
    CHOICES = [
        (key, key) for key in keys
    ]
class Payment(models.Model):
    """Model definition for Payment."""

    # TODO: Define fields here
    # does amount need to be positive number only
    amount = models.DecimalField(
        _("amount"), max_digits=7, decimal_places=2, default=Decimal("0.0"))
    # generate a unique id field
    # pid = models.UUIDField(_("pid"), primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey("enrollments.Enrollment", verbose_name=_("enrollment"),
                                   related_name="%(app_label)s_%(class)s_related",
                                   related_query_name="%(app_label)s_%(class)ss", on_delete=models.CASCADE)
    status = models.CharField(_("status"), max_length=32,
                              choices=PaymentStatus.CHOICES, default=PaymentStatus.INPROGRESS)
    created_at = models.DateTimeField(_("createdAt"), auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def change_status(self, new_status):
        self.status = new_status
        self.save()

    class Meta:
        """Meta definition for Payment."""

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        """Unicode representation of Payment."""
        return 'at {} price: {}'.format(self.created_at, self.amount)


class OnlinePayment(Payment):
    """Model for online based payment."""
    variant = models.CharField(_("variant"), choices=OnlinePaymentVariants.CHOICES, max_length=32, default='esewa')
    tax_amount = models.DecimalField(
        _("tax_amount"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    service_charge = models.DecimalField(
        _("service_charge"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    delivery_charge = models.DecimalField(
        _("delivery_charge"), max_digits=5, decimal_places=2, default=Decimal("0.0"))
    merchant_code = models.CharField(_("scd"), max_length=32)
    transaction_code = models.CharField(_("txcode"), max_length=128, null=True, blank=True)
    product_code = models.CharField(_("pid"), max_length=128)
    # this is the field to store extra content that may be present only
    # for one of the gateway
    extra_content = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        """Meta definition for esewa based payment."""
        verbose_name = 'OnlinePayment'
        verbose_name_plural = 'OnlinePayments'
        ordering = ['created_at']

    def capture(self, amount=None):
        gateway = gateway_factory.get_gateway(self.variant)
        status = self.status
        if status == PaymentStatus.PAID:
            status = gateway.capture(self, amount)
        self.change_status(status)
        print('******', self)





class BankPayment(Payment):
    """Model for bank based pay"""
    voucher = models.ImageField(
        _("voucher"), upload_to='vouchers/', blank=True, null=True)

    class Meta:
        "Meta definition for bank based payment."
        verbose_name = 'BankPayment'
        verbose_name_plural = 'BankPayments'
