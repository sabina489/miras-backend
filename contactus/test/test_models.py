from django.test import TestCase
from contactus.models import ContactUs

#ContactUs testcase
class ContactUse(TestCase):
    def create_Contact(self,name="contact",email="karkisabina869@gmail.com",send_status="200",message="contactus"):
        return ContactUs.objects.create(name=name, email=email,send_status=send_status,message=message)
    
    def test_Contact_creation(self):
        w = self.create_Contact()
        self.assertEqual(w.__str__(), w.name)
