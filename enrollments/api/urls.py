from django.urls import path

from enrollments.api.views import (
    EnrollmentCreateAPIView,
    EnrollmentDeleteAPIView,
    EnrollmentListAPIView,
    EnrollmentDetailAPIView,
)

urlpatterns = [
    path('create/', EnrollmentCreateAPIView.as_view(), name='create'),
    path('list/', EnrollmentListAPIView.as_view(), name='list'),
    path('details/<int:pk>/', EnrollmentDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', EnrollmentDeleteAPIView.as_view(), name='delete'),
]
