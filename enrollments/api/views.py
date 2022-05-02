from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from enrollments.models import (
    Enrollment,
    EnrollmentStatus,
)

from enrollments.api.serializers import(
    EnrollmentCreateSerializer,
    EnrollmentDeleteSerializer,
    EnrollmentRetrieveSerializer,
)

User = get_user_model()


class EnrollmentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentCreateSerializer
    queryset = Enrollment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(student=self.request.user)


class EnrollmentDeleteAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentDeleteSerializer
    queryset = Enrollment.objects.all()

    def perform_update(self, serializer):
        serializer.save(status=EnrollmentStatus.CANCELLED)


class EnrollmentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentRetrieveSerializer
    queryset = Enrollment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        # if self.request.user.is_superuser:
        #     return queryset
        return queryset.filter(student=self.request.user)


class EnrollmentDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentRetrieveSerializer
    queryset = Enrollment.objects.all()

    # def get_queryset(self):
    # queryset = super().get_queryset()
    # if self.request.user.is_superuser:
    # return queryset
    # return queryset.filter(student=self.request.user)
