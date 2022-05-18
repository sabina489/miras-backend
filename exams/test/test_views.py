from ast import arg
from unicodedata import category
from django.test import TestCase, Client
from django.urls import reverse
from courses.models import CourseCategory
from enrollments.models import Enrollment, ExamStatus
from exams.models import Exam,Question,Option,QuestionStatus
from courses.models import Course, CourseCategory
from django.contrib.auth import get_user_model
from exams.models import Exam
from part.models import Part
User = get_user_model()

# ExamListApiView Testcase
class ExamListAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user=User.objects.create(phone="9841053290")
        courseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=courseCategory, instructor=user,link="http://www.google.com", password="adf", status="insession", price="12.00")

    def test_Exam(self):
        url = reverse("exams")
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),0)

# ExamDetailAPIView Testcase
class ExamDetailAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone="9813209876")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=CourseCategory, instructor=user, link="http://www.facebook.com",password = "password", status="insession", price="11.00")

    def test_Exam(self):
        url = reverse("exam-detail",args=[2]) 
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# ExamStatusUpdateAPIView TestCase
class ExamStatusUpdateAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone="9813209876")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=CourseCategory, instructor=user, link="http://www.facebook.com",password = "password", status="insession", price="11.00")

    def test_Exam(self):
        url = reverse("exam-states-up",args=[2]) 
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# ExamStatusRetrieveAPIView TestCase
class ExamStatusRetrieveAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone = "9841023490")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=CourseCategory, instructor = user, link ="http://www.google.com",password = "password", status="insession", price="2.0")
    
    def test_Exam(self):
        url = reverse("exam-states-ret",args=[1000])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# MockExamDetailAPIView TestCase
class MockExamDetailAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone = "9841023490")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=CourseCategory, instructor = user, link ="http://www.google.com",password = "password", status="insession", price="2.0")
    
    def test_Exam(self):
        url = reverse("mock-detail",args=[100])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# GorkhaPatraExamDetailAPIView TestCase
class GorkhaPatraExamDetailAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone = "9841153490")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course", category=CourseCategory, instructor = user, link="http://www.google.com",password = "password",status="insession", price="1.9")
        
    def test_Exam(self):
        url = reverse('gorkha-detail',args=[5])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# MCQExamDetailAPIView TestCase
class MCQExamDetailAPIView(TestCase):
    def create_Exam(self,name="exam"):
        user = User.objects.create(phone = "9801234490")
        CourseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course", category=CourseCategory, instructor = user, link="http://www.google.com",password ="password",status="insession",price="0.0")
    
    def test_Exam(self):
        url = reverse('mcq-detail',args=[9909])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)
    



