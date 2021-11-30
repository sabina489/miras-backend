from django.urls import path

from enrollments.api.views import (
    EnrollmentCreateAPIView,
    EnrollmentDeleteAPIView,
    EnrollmentListAPIView
)

urlpatterns = [
    path('create/', EnrollmentCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', EnrollmentDeleteAPIView.as_view(), name='delete'),
    path('list/<int:student_id>/', EnrollmentListAPIView.as_view(), name='list-students'),
]
