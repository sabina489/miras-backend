from django.test import TestCase, Client
from django.urls import reverse
from payments.models import Payment
from enrollments.models import Enrollment
from django.contrib.auth import get_user_model
from exams.models import Exam
from part.models import Part
User = get_user_model()

# Payment Views TestCase
class PaymentTestCase(TestCase):
    def create_Payment(self,amount="0.0"):
        student = User.objects.create(phone="9821053490")
        enrollment = Enrollment.objects.create(student=student)
        return Payment.objects.create(amount=amount,enrollment=enrollment)

    def test_payment_list_view(self):
        w = self.create_Payment()
        url = reverse('online-create')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 401)
        

