from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags
import requests

def send_mail_common(template, context, to, subject):
    htmly = get_template(template)
    from_email = settings.EMAIL_HOST_USER
    html_content = htmly.render(context)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_otp(to, otp):
    sms_send_url = settings.OTP_SEND_URL
    params = {
        "token": settings.SMS_TOKEN,
        "from": settings.SMS_FROM,
        "to": to,
        "text": "Your OTP is {otp}".format(123456),
    }
    otp_send = requests.post(sms_send_url, data=params)
    if otp_send.status_code == 200:
        print("OTP sent successfully")
        return True
    print("OTP sent failed", otp_send.json())
    return False