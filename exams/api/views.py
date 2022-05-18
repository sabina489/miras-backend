from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
)
from rest_framework import filters


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from enrollments.permissions import IsEnrolledActive

from .serializers import (
    ExamSerializer,
    MockExamSerializer,
    MCQExamSerializer,
    GorkhapatraExamSerializer,
    ExamStatusUpdateSerializer,
    ExamStatusRetrieveSerializer,
)
from ..models import (
    Exam,
    MockExam,
    MCQExam,
    GorkhapatraExam,
)
from enrollments.models import (
    ExamStatus
)

class ExamListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    queryset = Exam.objects.all()

class MockExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = MockExamSerializer
    queryset = MockExam.objects.all()


class ExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class MCQExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = MCQExamSerializer
    queryset = MCQExam.objects.all()


class GorkhaPatraExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsEnrolledActive]
    serializer_class = GorkhapatraExamSerializer
    queryset = GorkhapatraExam.objects.all()


class ExamStatusUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamStatusUpdateSerializer
    queryset = ExamStatus.objects.all()


class ExamStatusRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamStatusRetrieveSerializer
    queryset = ExamStatus.objects.all()
