from unicodedata import category
from django.test import TestCase
from part.models import Part

from courses.models import Course, CourseCategory

from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()

# TestCase for Part Model
class PartTest(TestCase):
    def PartNew(self, name="part",price="100"):
        user = User.objects.create(phone="984105390")
        courseCategory = CourseCategory.objects.create(name="part")
        course = Course.objects.create(
            name=name, 
            instructor=user,
            password="password123",
            category=courseCategory,
            link ="http://www.google.com",
            price="100",
            status="pending" 
            )
        
        return Part.objects.create(name=name,price=price,course=course)
        
        
    def test_Part_creation(self):
        
        course = self.PartNew()
        # print(course.__str__(), course.name)
        self.assertEqual(course.__str__(), course.name)
        # w = self.create_PartTest
        # self.assertEqual(w.__str__(), w.course_name)



