from rest_framework import serializers
from contactus.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
