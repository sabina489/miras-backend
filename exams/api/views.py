# TODO: make a mock test visible

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from .serializers import (
    ExamSerializer,
    MockExamSerializer,
    MCQExamSerializer,
    GorkhapatraExamSerializer,
    QuestionStatusSerializer,
)
from ..models import (
    Exam,
    MockExam,
    MCQExam,
    GorkhapatraExam,
    QuestionStatus,
)

class ExamListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class MockExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MockExamSerializer
    queryset = MockExam.objects.all()

class MCQExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MCQExamSerializer
    queryset = MCQExam.objects.all()

class GorkhaPatraExamDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GorkhapatraExamSerializer
    queryset = GorkhapatraExam.objects.all()

class QuestionStatusCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionStatusSerializer
    queryset = QuestionStatus.objects.all()

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)
