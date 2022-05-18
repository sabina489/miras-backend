from django.test import TestCase, Client
from django.urls import reverse
from courses.models import Course
from courses.models import Course, CourseCategory, CourseRequest
import json

from notes.models import Note
from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()


#Course views TestCase
class CourseListTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(phone="9840016000")
        self.courseCategory_science = CourseCategory.objects.create(
            name="Science"
        )
        self.courseCategory_math = CourseCategory.objects.create(
            name="Math"
        )
        self.courseCategory_english = CourseCategory.objects.create(
            name="English"
        )
        self.course_biology = Course.objects.create(
            name="Biology",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )
        self.course_chemistry = Course.objects.create(
            name="Chemistry",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.chemistry.com",
            price=4000, 
            status="pending"
        )
        self.course_algebra = Course.objects.create(
            name="Algebra",
            instructor=user1,
            password="123", 
            category=self.courseCategory_math,
            link="http://www.math.com",
            price=4000, 
            status="pending"
        )
        self.course_geometry = Course.objects.create(
            name="Geometry",
            instructor=user1,
            password="123", 
            category=self.courseCategory_math,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )
        self.course_physics = Course.objects.create(
            name="Physics",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )

    def test_get_science_course(self):
        url = reverse("course-list", args=[self.courseCategory_science.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data), 3)
        self.assertIn(self.course_biology.name, resp.data[0]['name'])

    def test_get_math_course(self):
        url = reverse("course-list", args=[self.courseCategory_math.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data),2)
        self.assertIn(self.course_algebra.name, resp.data[0]['name'])

    def test_get_english_course(self):
        url = reverse("course-list", args=[self.courseCategory_english.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data), 0)

    def test_get_invalid_course(self):
        url = reverse("course-list", args=[40000])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data),0)
        
    def test_search_with_name_course(self):
        url = reverse("course-list", args=[self.courseCategory_science.id])
        url = url+"?search=Biology"
        resp = self.client.get(url)
        self.assertEquals(len(resp.data), 1)
        self.assertIn(self.course_biology.name, resp.data[0]['name'])
    

#CourseRetrieveAPIView TestCase
class CourseRetrieveAPIViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(phone="9840016000")
        self.courseCategory_science = CourseCategory.objects.create(
            name="Science"
        )
        self.courseCategory_math = CourseCategory.objects.create(
            name="Math"
        )
        self.courseCategory_english = CourseCategory.objects.create(
            name="English"
        )
        self.course_biology = Course.objects.create(
            name="Biology",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )
        self.course_chemistry = Course.objects.create(
            name="Chemistry",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.chemistry.com",
            price=4000, 
            status="pending"
        )
        self.course_algebra = Course.objects.create(
            name="Algebra",
            instructor=user1,
            password="123", 
            category=self.courseCategory_math,
            link="http://www.math.com",
            price=4000, 
            status="pending"
        )
        self.course_geometry = Course.objects.create(
            name="Geometry",
            instructor=user1,
            password="123", 
            category=self.courseCategory_math,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )
        self.course_physics = Course.objects.create(
            name="Physics",
            instructor=user1,
            password="123", 
            category=self.courseCategory_science,
            link="http://www.biology.com",
            price=4000, 
            status="pending"
        )

    def test_get_science_course(self):
        url = reverse("course-retrieve", args=[self.course_biology.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course_biology.name, resp.data['name'])

    def test_get_science_course(self):
        url = reverse("course-retrieve", args=[self.course_physics.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course_physics.name, resp.data['name'])

    def test_get_science_course(self):
        url = reverse("course-retrieve", args=[self.course_chemistry.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course_chemistry.name, resp.data['name'])

    def test_get_math(self):
        url = reverse("course-retrieve", args=[self.course_algebra.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course_algebra.name, resp.data['name'])
    
    def test_get_science_course(self):
        url = reverse("course-retrieve", args=[self.course_geometry.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course_geometry.name, resp.data['name'])
    
    
# Testcase for CourseCategoryListApiview
class CourseCategoryListAPIViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(phone="9840016000")
        self.courseCategory_science = CourseCategory.objects.create(
            name="Science"
        )
        self.courseCategory_math = CourseCategory.objects.create(
            name="Math"
        )
        self.courseCategory_english = CourseCategory.objects.create(
            name="English"
        )
        
    
    def test_get_course_category_lists(self):
        url = reverse("category-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertGreaterEqual(len(resp.data), 3)
        # print('********')
        # print(type(resp.data))
        # self.assertIn(self.course_biology.name, resp.data['name'])

# TestCase for CourseCategoryRetrieveAPIView 
class CourseCategoryRetrieveAPIViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(phone="9841053490")
        self.courseCategory_science = CourseCategory.objects.create(
            name="Science"
        )
        self.courseCategory_math = CourseCategory.objects.create(
            name="Math"
        )
        self.courseCategory_english = CourseCategory.objects.create(
            name="English"
        )
        

    def test_get_course_category_retrieve_view(self):
        url = reverse("category-retrieve", args=[self.courseCategory_science.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data), 3)
        # self.assertEqual(resp.status_code, 200)
        # print(resp.data)
        self.assertIn(self.courseCategory_science.name, resp.data['name'])
    
    def test_get_math_course(self):
        url = reverse("category-retrieve", args=[self.courseCategory_math.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data),3)
        self.assertIn(self.courseCategory_math.name, resp.data['name'])
    
    def test_get_math_course(self):
        url = reverse("category-retrieve", args=[self.courseCategory_english.id])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data),3)
        self.assertIn(self.courseCategory_english.name, resp.data['name'])
    
    def test_get_invalid_course(self):
        url = reverse("category-retrieve", args=[400])
        resp = self.client.get(url)
        self.assertEquals(len(resp.data),1)

    
        
    