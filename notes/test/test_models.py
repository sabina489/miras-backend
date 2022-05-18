from django.test import TestCase
from django.db import models 
from django.db.models.fields.related import ForeignKey
from notes.models import Note, Course
from courses.models import Course, CourseCategory

from part.models import Part
from django.contrib.auth import get_user_model
User = get_user_model()

# TestCase for Note models
class NoteTest(TestCase):
    def NoteNew(self,title="Note",body="Note",price="0.0"):
        user = User.objects.create(phone="9840018000")
        courseCategory = CourseCategory.objects.create(name="part")
        self.course = Course.objects.create(
            name="name", 
            instructor=user,
            password="password123",
            category=courseCategory,
            link ="http://www.google.com",
            price="100",
            status="pending" 
            )
        
        user = User.objects.create(phone="9840016000")
        
        part = Part.objects.create(
            name="part",
            course=self.course,
            price="10.0"

            )
        return Note.objects.create(title=title,body=body,price=price,courses=self.course,created_by=user,part=part)

    def test_Note_creation(self):
        w = self.NoteNew()
        self.assertEqual(w.__str__(), w.title)
        
    
