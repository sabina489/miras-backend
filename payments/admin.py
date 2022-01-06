from django.contrib import admin
from .models import (
    Payment,
    OnlinePayment,
    BankPayment,
)
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class OnlinePaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(OnlinePayment, OnlinePaymentAdmin)
