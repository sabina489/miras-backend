from django.contrib import admin
from contactus.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'message','send_status', 'created_on']


admin.site.register(ContactUs, ContactUsAdmin)
