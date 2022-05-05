from django.urls import path

from .views import (
    ExamListAPIView,
    ExamDetailAPIView,
    ExamStatusUpdateAPIView,
    ExamStatusRetrieveAPIView,
    MCQExamDetailAPIView,
    MCQExamMiniDetailAPIView,
    MockExamDetailAPIView,
    MockExamMiniDetailAPIView,
    GorkhaPatraExamDetailAPIView,
)

urlpatterns = [
    path('detail/<int:pk>/',
         ExamDetailAPIView.as_view(), name='exam-detail'),
    path('detail/mock/<int:pk>/',
         MockExamDetailAPIView.as_view(), name='mock-detail'),
    path('detail/mock/mini/<int:pk>/',
         MockExamMiniDetailAPIView.as_view(), name='mock-mini-detail'),
    path('detail/gorkha/<int:pk>/',
         GorkhaPatraExamDetailAPIView.as_view(), name='gorkha-detail'),
    path('detail/mcq/<int:pk>/', MCQExamDetailAPIView.as_view(), name='mcq-detail'),
    path('detail/mcq/mini/<int:pk>/',
         MCQExamMiniDetailAPIView.as_view(), name='mcq-mini-detail'),
    path('update/states/<int:pk>',
         ExamStatusUpdateAPIView.as_view(), name='exam-states-up'),
    path('list/', ExamListAPIView.as_view(), name='exams'),
    path('retrieve/states/<int:pk>',
         ExamStatusRetrieveAPIView.as_view(), name='exam-states-ret'),
]
