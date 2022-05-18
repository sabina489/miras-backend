from django.test import TestCase
from django.urls import reverse
from contactus.models import ContactUs

# Model test
#ContactUs testcase
# class ContactUse(TestCase):
#     def create_Contact(self,name="contact",email="karkisabina869@gmail.com",send_status="200",message="contactus"):
#         return ContactUs.objects.create(name=name, email=email,send_status=send_status,message=message)
    
#     def test_Contact_creation(self):
#         w = self.create_Contact()
#         self.assertEqual(w.__str__(), w.name)

# #views test
class ContactUsAPIViewTest(TestCase):
    def create_Contact(self,name="contact",email="karkisabina869@gmail.com",send_status="200",message="contactus"):
        return ContactUs.objects.create(name=name, email=email,send_status=send_status,message=message)
    
    def test_contact_list_view(self):
        w = self.create_Contact()
        url = reverse('contact_us_create')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 405)
        print(resp.data)

        # self.assertIn(w.name, resp.data)