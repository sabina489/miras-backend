from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.utils.translation import gettext, gettext_lazy as _

from accounts.models import Role, User, Profile
from common.utils import send_mail_common
from django.template.response import TemplateResponse
from enrollments.forms import EmailForm


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role')
    search_fields = ('phone', 'first_name', 'last_name', 'email')
    ordering = ('phone',)
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('phone', 'email', 'password', 'otp', 'otp_reset')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('otp_expiry', 'otp_reset_expiry', 'reset_token', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'role'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password1', 'password2'),
        }),
    )
    actions = ['send_email']

    def send_email(self, request, queryset):
        opts = self.model._meta
        app_label = opts.app_label
        context = {
            **self.admin_site.each_context(request),
            'title': "Send Email",
            'subtitle': None,
            'object_name': "Users",
            'object': queryset,
            'model_count': queryset.count(),
            'opts': opts,
            'app_label': app_label,
            'preserved_filters': self.get_preserved_filters(request),
            'items': queryset,
        }
        if 'apply' in request.POST:  # if user pressed 'apply' on intermediate page
            # Cool thing is that params will have the same names as in forms.py
            email_context = {
                "message": request.POST["message"],
            }
            subject = request.POST["subject"]

            # Run background task that will send broadcast messages
            for user in queryset:
                if to := user.email:
                    send_mail_common("admin/send_mail.html",
                                     email_context, [to], subject)

            # Show alert that everything is cool
            self.message_user(
                request, f"Message has been send to {queryset.count()} students")

            # Return to previous page
            return HttpResponseRedirect(request.get_full_path())

        # Create form and pass the data which objects were selected before triggering 'broadcast' action
        # We create an intermediate page right here
        form = EmailForm(
            initial={'_selected_action': queryset.values_list('id', flat=True)})
        context['form'] = form

        # We need to create a template of intermediate page with form - but this is really easy
        return TemplateResponse(request, "admin/email_data.html", context)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Profile)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
