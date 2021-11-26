from django.urls import path

from enrollments.api.views import EnrollmentCreateAPIView

urlpatterns = [
    path('create/', EnrollmentCreateAPIView.as_view(), name='create'),
]
