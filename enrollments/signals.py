from django.db.models.signals import post_save
from django.dispatch import receiver
from courses.models import CourseStatus
from enrollments.api.utils import end_enrollment


@receiver(post_save, sender='courses.Course')
def on_course_end(sender, instance, **kwargs):
    if instance.status == CourseStatus.ENDED:
        ended_enrolls = end_enrollment(instance)
        print('these enrollments have ended : \n', ended_enrolls)