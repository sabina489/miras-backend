from django.contrib.auth import get_user_model
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

from enrollments.models import (
    Enrollment,
)

from enrollments.api.serializers import(
    EnrollmentCreateSerializer
)

User = get_user_model()

class EnrollmentCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EnrollmentCreateSerializer
    queryset = Enrollment.objects.all()
