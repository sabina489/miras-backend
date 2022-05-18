from unicodedata import category
from django.test import TestCase
from courses.models import CourseCategory
from enrollments.models import Enrollment, ExamStatus
from exams.models import Exam,Question,Option,QuestionStatus
from courses.models import Course, CourseCategory
from django.contrib.auth import get_user_model
from exams.models import Exam
from part.models import Part
User = get_user_model()

#exam model TestCase
class ExamTestCase(TestCase):
    def create_Exam(self,name="exam"):
        user=User.objects.create(phone="9841053290")
        courseCategory = CourseCategory.objects.create(name="exam")
        course = Course.objects.create(name="course1", category=courseCategory, instructor=user,link="http://www.google.com", password="adf", status="insession", price="12.00")
        
        return Exam.objects.create(name=name,course=course)
    
    def test_creation(self):
        w = self.create_Exam()
        self.assertEqual(w.__str__(),w.name)

# Question model TestCase
class QuestionTestCase(TestCase):
    def create_Question(self,detail="question"):
        exam = Exam.objects.create(name="question")
        return Question.objects.create(exam=exam)

    def test_Question_creation(self):
        w = self.create_Question()
        self.assertEqual(w.__str__(),"{}_{}".format(w.exam, w.id))
    

# Option model TestCase
class OptionTestCase(TestCase):
    def create_Option(self,detail="option",correct=True,marks="0.0"):
        exam = Exam.objects.create(name="question")
        self.question = Question.objects.create(detail="option",marks="0.0",exam=exam)
        return Option.objects.create(detail=detail,correct=correct,question=self.question,marks=marks)
    
    def test_Option_creation(self):
        w = self.create_Option()
        self.assertEqual(w.__str__(),"{}_{}".format(w.question, w.id))

#QuestionStatus model TestCase
class QuestionStatusTestCase(TestCase):
    def create_Question_Status(self):
        user=User.objects.create(phone="9841053290")
        enrollment=Enrollment.objects.create(student=user)
        exam=Exam.objects.create(name="question")
        exam_stat = ExamStatus.objects.create(exam=exam,enrollment=enrollment)
        # exam = Exam.objects.create(name="question")
        question = Question.objects.create(detail="option",marks="0.0",exam=exam)
        selected_option = Option.objects.create(detail="detail", question=question)
        return QuestionStatus.objects.create(exam_stat=exam_stat,question=question,selected_option=selected_option)
    
    def test_Question_Status_creation(self):
        w = self.create_Question_Status()
        self.assertEqual(w.__str__(),"option {} by {} for {}".format(w.exam_stat,w.question,w.selected_option))
        


        
