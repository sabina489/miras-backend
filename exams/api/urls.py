from django.urls import path

from .views import (
    ExamListAPIView,
    MCQExamDetailAPIView,
    MockExamDetailAPIView,
    GorkhaPatraExamDetailAPIView,
    QuestionStatusCreateAPIView,
)

urlpatterns = [
    path('detail/mock/<int:pk>/', MockExamDetailAPIView.as_view(), name='mock-detail'),
    path('detail/gorkha/<int:pk>/', GorkhaPatraExamDetailAPIView.as_view(), name='gorkha-detail'),
    path('detail/mcq/<int:pk>/', MCQExamDetailAPIView.as_view(), name='mcq-detail'),
    path('create/states/', QuestionStatusCreateAPIView.as_view(), name='question-states'),
    path('list/', ExamListAPIView.as_view(), name='exams'),
]
