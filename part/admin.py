from django.contrib import admin

from part.models import (
    Part,
)

class PartAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'course', 'price', 'detail',)
    list_filter = ('course',)


# Register your models here.
admin.site.register(Part, PartAdmin)
