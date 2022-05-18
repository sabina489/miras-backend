from unicodedata import category
from django.test import TestCase, Client
from django.urls import reverse
from django.db import models
from django.db.models.fields.related import ForeignKey
from notes.models import Note, Course
from courses.models import Course, CourseCategory

from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()

# NoteCreateAPIView TestCase
class NoteCreateAPIViewTest(TestCase):
    def create_Note(self,title="Note",body="Note",price="0.0"):
        user = User.objects.create(phone="9812345670")
        CourseCategory = CourseCategory.objects.create(name="part")
        self.course = Course.objects.create(name="name",instructor=user,password="password",category=CourseCategory,link="http://www.google.com",price="100",status="pending")
        user= User.objects.create(phone="9809876543")
        part = Part.objects.create(name="part",course=self.course,price="0.0")
    
    def test_Note(self):
        url = reverse("create")
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)

# NoteListAPIView TestCase
class NoteListAPIViewTest(TestCase):
    def create_Note(self,title="Note",body="Note",price="1.0"):
        user = User.objects.create(phone="9812340987")
        CourseCategory = CourseCategory.objects.create(name="part")
        self.course = Course.objects.create(name="name", instructor=user,password="password124",category=CourseCategory,link="http://www.google.com",price="100",status="pending")
        user = User.objects.create(phone = "9860776448")
        part = Part.objects.create(name="part",course=self.course,price="2.0")

    def test_Note(self):
        url = reverse("list")
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),0)

# NoteRetrieveAPIView TestCase
class NoteRetrieveAPIViewTest(TestCase):
    def create_Note(self,title="Note", body="Note",price="2.0"):
        user = User.objects.create(phone="9849777210")
        CourseCategory = CourseCategory.objects.create(name="part")
        self.course = Course.objects.create(name="name", instructor=user,password="password",category=CourseCategory,link="http://www.google.com",price="200",status = "pending")
        user = User.objects.create(phone = "9831054490")
        part = Part.objects.create(name="part",course=self.course,price="2.0")
    
    def test_Note(self):
        url = reverse("detail", args=[1])
        resp = self.client.get(url)
        self.assertEqual(len(resp.data),1)