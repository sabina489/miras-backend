from django.db import models

# Create your models here.


class OTP(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.IntegerField()
    otp_expiry = models.DateTimeField()
    result = models.TextField()
    error_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone}"
