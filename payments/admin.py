from django.contrib import admin
from .models import (
    Payment,
    OnlinePayment,
    BankPayment,
)
# Register your models here.

class OnlinePaymentInline(admin.TabularInline):
    model = OnlinePayment
    extra = 0

class BankPaymentInline(admin.TabularInline):
    model = BankPayment
    extra = 0


# class PaymentAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)
#     list_display = ('id', 'enrollment', 'amount',
#                     'status', 'created_at', 'updated_at')
#     list_filter = ('status',)


class OnlinePaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'enrollment', 'amount',
                    'status', 'created_at', 'updated_at')
    list_filter = ('status',)

class BankPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)



# admin.site.register(Payment, PaymentAdmin)
admin.site.register(OnlinePayment, OnlinePaymentAdmin)
admin.site.register(BankPayment, BankPaymentAdmin)