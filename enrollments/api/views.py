from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)

from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.utils import serializer_helpers

from enrollments.models import (
    Enrollment,
)

from enrollments.api.serializers import(
    EnrollmentCreateSerializer,
    EnrollmentDeleteSerializer,
    EnrollmentRetrieveSerializer,
)

User = get_user_model()


class EnrollmentCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EnrollmentCreateSerializer
    queryset = Enrollment.objects.all()


class EnrollmentDeleteAPIView(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = EnrollmentDeleteSerializer
    queryset = Enrollment.objects.all()


class EnrollmentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EnrollmentRetrieveSerializer
    def get_queryset(self):
        queryset = Enrollment.objects.all()
        student_id = self.kwargs['student_id']
        return queryset.filter(student=student_id)