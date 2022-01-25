from django.contrib import admin
from django.forms import ModelForm
from content.models import Content


class ContentAdminForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        widgets = {
            'description': admin.widgets.AdminTextareaWidget(attrs={"rows": 2, "cols": 1})
        }


class ContentInline(admin.TabularInline):
    model = Content
    form = ContentAdminForm
    extra = 1
    show_change_link = True
    readonly_fields = ('created_by',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'note', 'created_at', 'created_by']
    list_filter = ['created_at', 'note']
    search_fields = ['name', 'description']

    def save_model(self, request, obj, form, change):
        if not change:
            if not hasattr(obj, 'created_by'):
                obj.created_by = request.user
        obj.save()


admin.site.register(Content, ContentAdmin)
