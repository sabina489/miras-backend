from django.test import TestCase, Client
from django.urls import reverse
from courses.models import CourseCategory,Course
from part.models import Part

import json

from notes.models import Note,Course
from django.contrib.auth import get_user_model
User = get_user_model()

# PartListAPIView Testcase
class PartListAPIViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(phone="9840015609")
        # part=Course.objects.create(name="part")
        courseCategory = CourseCategory.objects.create(name="math")
        self.course = Course.objects.create(
            name="name", 
            instructor=user,
            password="password123",
            category=courseCategory,
            link ="http://www.google.com",
            price="100",
            status="pending" 
            )
        self.part = Part.objects.create(name="name",course=self.course)
        
        
        # self.part = Part.objects.create(name="part")

    
    def test_get_part(self):
        url = reverse('part-list', args=[self.course.id])
        resp = self.client.get(url)
        print('***************')
        print(resp.data)
        # self.assertEquals(len(resp))
        self.assertIn(self.part.name, resp.data[0]['name'])

