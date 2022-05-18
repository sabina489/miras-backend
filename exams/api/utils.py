from doctest import Example
from django.db import models


def calculate_full_marks(obj):
    """Calculate total marks for a exam.
    >>> calculate_full_marks(MockExam.objects.get(id=1))
    calculated by adding all the marks of questions in the exam.

    Args:
        obj (exam): Mock or MCQ exam object 

    Returns:
        decimal: total marks 
    """
    return obj.questions.aggregate(full_marks=models.Sum('marks'))['full_marks']
