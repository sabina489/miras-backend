from django.urls import path

from .views import (
    ExamListAPIView,
    ExamStatusUpdateAPIView,
    ExamStatusRetrieveAPIView,
    MCQExamDetailAPIView,
    MockExamDetailAPIView,
    GorkhaPatraExamDetailAPIView,
    # QuestionStatusCreateAPIView,
    # ExamStatusRetrieveAPIView,
    # QuestionStatusRetrieveAPIView,
)

urlpatterns = [
    path('detail/mock/<int:pk>/', MockExamDetailAPIView.as_view(), name='mock-detail'),
    path('detail/gorkha/<int:pk>/', GorkhaPatraExamDetailAPIView.as_view(), name='gorkha-detail'),
    path('detail/mcq/<int:pk>/', MCQExamDetailAPIView.as_view(), name='mcq-detail'),
    # path('create/states/', QuestionStatusCreateAPIView.as_view(), name='question-states'),
    path('update/states/<int:pk>', ExamStatusUpdateAPIView.as_view(), name='exam-states-up'),
    path('list/', ExamListAPIView.as_view(), name='exams'),
    path('retrieve/states/<int:pk>', ExamStatusRetrieveAPIView.as_view(), name='exam-states-ret'),
    # path('question/states/<int:pk>', QuestionStatusRetrieveAPIView.as_view()),
]
