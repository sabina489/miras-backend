from django.contrib import admin

from courses.models import (
    Course,
    CourseCategory
)
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class CourseCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory, CourseCategoryAdmin)