from django.test import TestCase
from unicodedata import category
from django.test import TestCase
from django.db import models
from django.utils import timezone
from courses.models import Course, CourseCategory, CourseRequest

from notes.models import Note
from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()

# CourseCategory Model TestCase
# class CourseCategoryTestCase(TestCase):
#     def create_CourseCategory(self, name="text",parent="parent"):
#         #user = User.objects.create(phone="9840016000")
#         #courseCategory = CourseCategory.parent.create(name="ad")
#         return CourseCategory.objects.create(name=name,parent=parent)

#     def test_CourseCategory_creation(self):
#         w = self.create_CourseCategory()
#         self.assertEqual(w.__str__(), w.name)


#Course  Testcase
class CourseTestCase(TestCase):
    def CourseNew(self, name="text",instructor="instructor",password="text",status="status" ,link="http://www.google.com",thumbnail = "thumbnail", main_detail="describe"):
        user = User.objects.create(phone="9840016000")
        courseCategory = CourseCategory.objects.create(name="ad")
        return Course.objects.create(name=name, instructor=user,password=password, category=courseCategory,link=link,price=4000, status="pending")

    def test_Course_creation(self):
        
        # w = self.create_Course()   link="http://www.google.com",
        # self.assertEqual(w.__str__(), w.name)
        courseNew= self.CourseNew()
        # print(courseNew.__str__(), courseNew.link)
        self.assertEqual(courseNew.__str__(), courseNew.name)


#CourseRequest Testcase
class CourseRequestTestCase(TestCase):
    def create_CourseRequest(self, course_name="text", course_category="123", requester_name="text", requester_email="karkisabina869@gmail.com"):
        return CourseRequest.objects.create(course_name=course_name,course_category=course_category,requester_email=requester_email)
        
    def test_CourseRequest_creation(self):
        w = self.create_CourseRequest()
        self.assertEqual(w.__str__(), w.course_name)