from django.contrib import admin

from courses.models import (
    Course,
    CourseCategory
)
# Register your models here.


class CourseAdmin(admin.ModelAdmin):

    def date_time(self, obj):
        return f"{obj.start_date} - {obj.end_date}"

    readonly_fields = ('id',)
    list_display = ('id', 'name', 'category', 'instructor',
                    'status', 'price', 'date_time')
    list_filter = ('status', 'category')


class CourseCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'parent')
    list_filter = ('parent',)


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)
