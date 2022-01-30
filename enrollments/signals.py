from django.db.models.signals import post_save
from django.dispatch import receiver
from courses.models import CourseStatus
from payments.models import PaymentStatus
from enrollments.models import ExamStatus
from enrollments.api.utils import (
    end_enrollment,
    activate_enrollment
)


@receiver(post_save, sender='courses.Course')
def on_course_end(sender, instance, **kwargs):
    if instance.status == CourseStatus.ENDED:
        ended_enrolls = end_enrollment(instance)


@receiver(post_save, sender='payments.OnlinePayment')
def on_paid_status(sender, instance, **kwargs):
    if instance.status == PaymentStatus.PAID:
        activated_enroll = activate_enrollment(instance)
        print('activated enrollment', activated_enroll)


@receiver(post_save, sender='payments.BankPayment')
def on_paid_status(sender, instance, **kwargs):
    if instance.status == PaymentStatus.PAID:
        activated_enroll = activate_enrollment(instance)
        print('activated enrollment', activated_enroll)
