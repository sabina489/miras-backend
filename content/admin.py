from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from content.models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'free', 'course', 'part', 'created_at']
    list_filter = ['created_at', 'course', 'part']
    search_fields = ['name', 'description']


admin.site.register(Content, ContentAdmin)
