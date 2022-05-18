# from django.test import TestCase, Client
# from django.urls import reverse
# from content.models import Content, RecordedVideo
# import json

# from notes.models import Note
# from part.models import Part
# from django.contrib.auth import get_user_model
# User = get_user_model()

# # Views testcase for ContentCourseListAPIView
# class ContentCourseListAPIViewTest(TestCase):
#     def setUp(self):
#         user1 = User.objects.create(phone="9840016000")
#         self.courseCategory_science = Content.objects.create(
#             name="Science"
#         )
#         self.courseCategory_math = Content.objects.create(
#             name="Math"
#         )
#         self.courseCategory_english = Content.objects.create(
#             name="English"
#         )
#         self.course_biology = Content.objects.create(
#             name="Biology",
#             instructor=user1,
#             password="123", 
#             category=self.courseCategory_science,
#             link="http://www.biology.com",
#             price=4000, 
#             status="pending"
#         )
#     def test_get_science_course(self):
#         url = reverse("course-list", args=[self.courseCategory_science.id])
#         resp = self.client.get(url)
#         self.assertEquals(len(resp.data), 3)
#         self.assertIn(self.course_biology.name, resp.data[0]['name'])
