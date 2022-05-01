from django.core.mail import send_mail
from django import forms


class EmailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
