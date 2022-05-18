from tkinter import PhotoImage
from django.test import TestCase
import enrollments
from enrollments.models import Enrollment, ExamStatus
from django.db import models
from django.contrib.auth import get_user_model
from exams.models import Exam
from part.models import Part
User = get_user_model()

# Enrollment models TestCase
class EnrollmentTestCase(TestCase):
    def create_Enrollment(self, student="text",status="status"):
        self.student = User.objects.create(phone="9841053490") 
        return Enrollment.objects.create(student=self.student)
        
    def test_creation(self):
        w = self.create_Enrollment()
        self.assertEqual(
            w.__str__(), 
            "{} at {}".format(w.student.__str__(),w.created_at)
        )
        self.assertEqual(
            w.student,
            self.student
        )

#ExamStatus TestCase
class ExamStatusTestCase(TestCase):
    def create_ExamStatus(self, enrollment="enrollment",exam="exam"):
        self.student = User.objects.create(phone="9841053490") 
        enrollment=Enrollment.objects.create(student=self.student)
        exam = Exam.objects.create(name="exam")
        return ExamStatus.objects.create(exam=exam,enrollment=enrollment)
        
    def test_ExamStatus_creation(self):
        w = self.create_ExamStatus()
        self.assertEqual(w.__str__(), "enrollment {} for exam {}".format(w.enrollment,w.exam))