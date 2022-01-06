from enrollments.models import (
    Enrollment,
    EnrollmentStatus
)


def count_enrollments(enrolled_obj):
    """Count the number of enrollments.

    Args:
        enrolled_obj (parts/notes/course/tests): [description]

    Returns:
        int: number of enrollments for that object
    """
    # lets assume obj is only parts
    count = enrolled_obj.enrolls.count()

    return count

def activate_enrollment(payment):
    """Change enrollment status to active.

    Args:
        payment (payment object): instance of Payment model

    Returns:
        enrollment: instance of Enrollment model
    """
    enroll = payment.enrollment
    enroll.status = EnrollmentStatus.ACTIVE
    enroll.save()
    return enroll

def end_enrollment(ended_class):
    """End all enrollment of class.
    Changes the status of enrollment to inactive
    when the class ends.

    Args:
        ended_class (Course): Course that has ended.

    Returns:
        list: list of cancelled enrollments
    """
    cancelled_enrolls = []
    for part in ended_class.parts.all():
        for enroll in part.enrolls.all():
            enroll.status = EnrollmentStatus.INACTIVE
            enroll.save()
            cancelled_enrolls.append(enroll)
    return cancelled_enrolls


def is_enrolled(enrolled_obj, user):
    """Return enrollment status of the user for that obj.

    Args:
        enrolled_obj (part/note/exam): obj to which user is enrolled into
        user (user): whose enrollment is to be checked

    Returns:
        bool: state of enrollment of user to that obj
    """
    enrollments = []
    if user.is_authenticated:
        enrollments = enrolled_obj.enrolls.all().filter(
            student=user)
    if len(enrollments) > 0:
        return True
    return False

def is_enrolled_active(enrolled_obj, user):
    """Return enrollment status of the user for that obj.

    Args:
        enrolled_obj (part/note/exam): obj to which user is enrolled into
        user (user): whose enrollment is to be checked

    Returns:
        bool: state of enrollment of user to that obj
    """
    enrollments = []
    if user.is_authenticated:
        enrollments = enrolled_obj.enrolls.all().filter(
            student=user, status=EnrollmentStatus.ACTIVE)
    if len(enrollments) > 0:
        return True
    return False
