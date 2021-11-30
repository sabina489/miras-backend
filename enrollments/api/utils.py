

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
