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
