from unicodedata import category
from django.test import TestCase
from content.models import Content, RecordedVideo
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from courses.models import Course, CourseCategory

from notes.models import Note
from part.models import Part

User = get_user_model()
#Content TestCase
class ContentTestCase(TestCase):

    def create_Content(self, name="text", description="describe", type="pdf", file="file", note="note"):
        user = User.objects.create(phone="9840016000")
        courseCategory = CourseCategory.objects.create(name="ad")
        course = Course.objects.create(name="course1", category=courseCategory, instructor=user,
                                       link="http://www.google.com", password="adf", status="insession", price="12.00")
        part = Part.objects.create(
            name="part1", course=course, detail="asdf", price="12.00")
        note = Note.objects.create(
            title="Note1;", body="adsf", price="12.0", created_by=user, courses=course, part=part)
        return Content.objects.create(name=name, description=description, type=type, note=note, created_by=user)

    def test_Content_creation(self):
        w = self.create_Content()
        # print('checking', w,w,w.__str__())
        self.assertEqual(w.__str__(), w.name)


#Recorded TestCase
class RecordedVideoTestCase(TestCase):
    def create_RecordedVideo(self, name="text", file="pdf", part="part", created_by="now"):
        user = User.objects.create(phone="1244")
        courseCategory = CourseCategory.objects.create(name="ad")
        course = Course.objects.create(name="course", category=courseCategory, instructor=user, link="http://www,google.com",password="password", status="insession",price="12")
        part = Part.objects.create(name="part1", course=course, detail="asdf", price="12.00")
        return RecordedVideo.objects.create(name=name,part=part,created_by=user)
        
    def test_RecordedVideo_creation(self):
        w = self.create_RecordedVideo()
        self.assertEqual(w.__str__(), f"{w.name} - {w.part.name}")
