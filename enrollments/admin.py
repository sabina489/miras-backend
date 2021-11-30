from django.contrib import admin
from enrollments.models import (
    Enrollment
)
class EnrollmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(Enrollment, EnrollmentAdmin)