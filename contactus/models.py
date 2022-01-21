from django.db import models
from common.utils import send_mail_common
from django.conf import settings
import sys
import traceback


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    send_status = models.BooleanField(default=False)
    error = models.TextField(blank=True, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def send_mail(self):
        try:
            send_mail_common(
                'contactus/email.html',
                {
                    'name': self.name,
                    'email': self.email,
                    'message': self.message
                },
                [settings.EMAIL_HOST_USER],
                "Contact Us Mail"
            )
            status = True
            self.send_status = True 
        except BaseException as e:
            status = True
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)
            self.error = f"{ex_type}\n{ex_value}\n{trace_back}"

    def save(self, *args, **kwargs):
        self.send_mail()
        super().save(*args, **kwargs)