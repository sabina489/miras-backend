from django.contrib import admin
from common.models import OTP


class OTPAdmin(admin.ModelAdmin):
    list_display = ('phone', 'otp', 'otp_expiry',
                    'error_status', 'result', 'created_on')


admin.site.register(OTP, OTPAdmin)
