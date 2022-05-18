from django.test import TestCase
from enrollments.models import Enrollment, ExamStatus
from django.db import models
from exams.models import Exam


# Enrollment models TestCase
# class EnrollmentTestCase(TestCase):
#     def create_Enrollment(self, student="text",status="status"):
#         return Enrollment.objects.create()
        
#     def test_creation(self):
#         w = self.create_Enrollment()
#         self.assertEqual(w.__str__(), w.course_student)

# class ExamStatusTestCase(TestCase):
#     def create_ExamStatus(self, enrollment="enrollment",exam="exam",score="1"):
#         exam = Exam.objects.create()
#         return ExamStatus.objects.create(exam=exam, score=score)
        
#     def test_ExamStatus_creation(self):
#         w = self.create_ExamStatus()
#         self.assertEqual(w.__str__(), w.exam)