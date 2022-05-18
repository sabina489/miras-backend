from django.test import TestCase
from payments.models import OnlinePayment, Payment
from enrollments.models import Enrollment
from django.contrib.auth import get_user_model
from exams.models import Exam
from part.models import Part
User = get_user_model()

# Payment Model TestCase
class PaymentTestCase(TestCase):
    def create_Payment(self,amount="0.0"):
        student = User.objects.create(phone="9841023490")
        enrollment = Enrollment.objects.create(student=student)
        return Payment.objects.create(amount=amount,enrollment=enrollment)
    
    def test_Payment_creation(self):
        w = self.create_Payment()
        self.assertEqual(w.__str__(),'at {} price: {}'.format(w.created_at,w.amount))