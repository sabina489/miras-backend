from django.contrib import admin
from common.models import OTP

admin.site.site_header = "Miras Academy"
admin.site.site_title = "Miras Academy"
admin.site.index_title = "Miras Academy Dashboard"


class OTPAdmin(admin.ModelAdmin):
    list_display = ('phone', 'otp', 'otp_expiry',
                    'error_status', 'result', 'created_on')


admin.site.register(OTP, OTPAdmin)
