from django.test import TestCase, Client
from django.urls import reverse
from courses.models import CourseCategory,Course
from enrollments.models import Enrollment, ExamStatus
import json

from notes.models import Note
from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()

#Enrollment views TestCase
class EnrollmentCreateAPIViewTest(TestCase):
    def create_Enrollment(self,status="status"):
        self.student = User.objects.create(phone="9841053490")
    
        # self.courseCategory = CourseCategory.objects.create(name="enrollment")
    
    def test_Enrollment(self):
        url = reverse("create")
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)
        # self.assertIn(self.student.name, resp.data[0]['name'])

# EnrollmentDeleteAPIView TestCase
# class EnrollmentDeleteAPIViewTest(TestCase):
#     def create_Enrollment(self,status="status"):
#         self.student = User.objects.create(phone="9841053490")
    
#     def test_Enrollment_Delete_API_View(self):
#         url = reverse("delete", args=[1])
#         resp = self.client.get(url)
#         self.assertEqual(len(resp.data),1)
#         self.assertIn(self.student.name, resp.data[0]['name'])
#         print(resp.data)


#  EnrollmentListAPIView TestCase
# class EnrollmentListAPIViewTest(TestCase):
#     def create_Enrollment(self,status="status"):
#         self.student = User.objects.create(phone="9841053490")

#     def test_Enrollment_List_API_View(self):
#         url = reverse('list')
#         resp = self.client.get(url)
#         self.assertEqual(len(resp.data),0)
#         print(resp.data)

# #EnrollmentDetailAPIView TestCase
# class EnrollmentDetailAPIViewTest(TestCase):
#     def create_Enrollment(self,status="status"):
#         self.student = User.objects.create(phone="9841053490")
    
#     def test_Enrollment_Detail_API_View(self):
#         url = reverse("detail")
#         resp = self.client.get(url)
#         self.assertEqual(len(resp.data),0)
#         print(resp.data)
#         self.assertIn(self.student.name, resp.data[0]['name'])

