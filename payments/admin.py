from django.contrib import admin
from .models import (
    Payment,
    OnlinePayment,
    BankPayment,
)
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'enrollment', 'amount',
                    'status', 'created_at', 'updated_at')
    list_filter = ('status',)


class OnlinePaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'enrollment', 'amount',
                    'status', 'created_at', 'updated_at')
    list_filter = ('status',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(OnlinePayment, OnlinePaymentAdmin)
