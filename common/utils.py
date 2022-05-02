from unittest import result
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags
import requests
from miras.celery import app
from common.models import OTP


def send_mail_common(template, context, to, subject):
    htmly = get_template(template)
    from_email = settings.EMAIL_HOST_USER
    html_content = htmly.render(context)
    text_content = strip_tags(html_content)
    # msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    async_send_mail.delay(subject, text_content, from_email, to, html_content)


@app.task
def async_send_mail(subject, text_content, from_email, to, html_content):
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@app.task
def send_otp(to, otp, otp_expiry):
    otp_object = OTP.objects.create(
        phone=to, otp=otp, otp_expiry=otp_expiry, result="")
    sms_send_url = settings.OTP_SEND_URL
    params = {
        "auth_token": settings.SMS_TOKEN,
        "to": to,
        "text": f"Welcome to Miras Academy!! Your OTP is {otp}",
    }
    otp_send = requests.post(sms_send_url, data=params)
    result = otp_send.json()
    otp_object.result = result
    otp_object.error_status = result['error']
    otp_object.save()
    if not result['error']:
        return True
    return False
